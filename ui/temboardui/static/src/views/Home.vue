<script setup>
// Global: clearError, showError
import { useFullscreen } from "@vueuse/core";
import { Popover, Tooltip } from "bootstrap";
import $ from "jquery";
import _ from "lodash";
import moment from "moment";
import { computed, nextTick, onMounted, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

import InstanceCard from "../components/home/InstanceCard.vue";

const root = ref(null);
const instanceCards = ref(null);
const route = useRoute();
const router = useRouter();

const loading = ref(false);
const instances = ref([]);
const search = ref(route.query.q);
const sort = ref(route.query.sort || "status");
const environmentsFilter = ref(route.query.environments ? route.query.environments.split(",") : []);
const start = ref(moment().subtract(1, "hours"));
const end = ref(moment());
const refreshDate = ref(null);
const refreshInterval = ref(3 * 1000);
let popoverList = [];
let tooltipList = [];

const { toggle } = useFullscreen(root);

const props = defineProps(["isAdmin", "environments"]);

const filteredInstances = computed(() => {
  const searchRegex = new RegExp(search.value, "i");
  const filtered = instances.value.filter((instance) => {
    return (
      searchRegex.test(instance.hostname) ||
      searchRegex.test(instance.agent_address) ||
      searchRegex.test(instance.pg_data) ||
      searchRegex.test(instance.pg_port) ||
      searchRegex.test(instance.pg_version) ||
      searchRegex.text(instance.environment)
    );
  });
  let sorted;
  if (sort.value == "status") {
    sorted = sortByStatus(filtered);
  } else {
    sorted = _.sortBy(filtered, sort.value, "asc");
  }

  return sorted.filter((instance) => {
    if (!environmentsFilter.value.length) {
      return true;
    }
    return environmentsFilter.value.indexOf(instance.environment) != -1;
  });
});

onMounted(() => {
  refreshCards();
  window.setInterval(refreshCards, refreshInterval.value);
  nextTick(() => {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    [...tooltipTriggerList].map((el) => new Tooltip(el, { sanitize: false }));
  });
});

function toggleEnvironmentFilter(environment, e) {
  e.preventDefault();
  var index = environmentsFilter.value.indexOf(environment);
  if (index != -1) {
    environmentsFilter.value.splice(index, 1);
  } else {
    environmentsFilter.value.push(environment);
  }
}
function changeSort(value, e) {
  e.preventDefault();
  sort.value = value;
}

function fetchInstances() {
  clearError();
  $.ajax("/json/instances/home")
    .done((data) => {
      popoverList.forEach((p) => p.dispose());
      tooltipList.forEach((t) => t.dispose());
      instances.value = data;
      nextTick(() => {
        const popoverTriggerList = root.value.querySelectorAll('[data-bs-toggle="popover"]');
        popoverList = [...popoverTriggerList].map((el) => new Popover(el, { sanitize: false }));
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltipList = [...tooltipTriggerList].map((el) => new Tooltip(el, { sanitize: false }));
      });
    })
    .fail((xhr) => {
      showError(xhr);
    });
}

function refreshCards() {
  loading.value = true;
  fetchInstances();
  end.value = moment();
  start.value = moment().subtract(1, "hours");
  nextTick(() => {
    for (let i in instanceCards.value) {
      const card = instanceCards.value[i];
      if (i >= 18) {
        break;
      }
      card.fetchLoad1();
      card.fetchTPS();
    }
    refreshDate.value = moment();
    loading.value = false;
  });
}

function sortByStatus(items) {
  return items.sort(function (a, b) {
    return getStatusValue(b) - getStatusValue(a);
  });
}

/*
 * Util to compute a global status value given an instance
 */
function getStatusValue(instance) {
  var checks = getChecksCount(instance);
  var value = 0;
  if (checks.CRITICAL) {
    value += checks.CRITICAL * 1000000;
  }
  if (checks.WARNING) {
    value += checks.WARNING * 1000;
  }
  if (checks.UNDEF) {
    value += checks.UNDEF;
  }
  return value;
}

function getChecksCount(instance) {
  var count = _.countBy(
    instance.checks.map(function (state) {
      return state.state;
    }),
  );
  return count;
}

watch(search, (newVal) => {
  router.replace({
    query: _.assign({}, route.query, { q: newVal }),
  });
});
watch(sort, (newVal) => {
  router.replace({
    query: _.assign({}, route.query, { sort: newVal }),
  });
});
watch(environmentsFilter.value, (newVal) => {
  router.replace({
    query: _.assign({}, route.query, { environments: newVal.join(",") }),
  });
});
</script>

<template>
  <div ref="root">
    <div class="position-absolute" style="z-index: 2; right: 0">
      <button id="fullscreen" class="btn btn-link" @click="toggle">
        <i class="fa fa-expand"></i>
      </button>
    </div>
    <div class="row pb-3">
      <div class="col d-flex">
        <input type="text" class="form-control me-sm-2 w-auto" placeholder="Search instances" v-model="search" />
        <div class="dropdown me-sm-2">
          <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown">
            Sort by: <strong v-cloak>{{ sort }}</strong>
            <span class="caret"></span>
          </button>
          <div class="dropdown-menu" role="menu">
            <a class="dropdown-item" href v-on:click="changeSort('hostname', $event)">
              <i v-bind:class="['fa fa-fw', { 'fa-check': sort == 'hostname' }]"></i>
              Hostname
            </a>
            <a class="dropdown-item" href v-on:click="changeSort('status', $event)">
              <i v-bind:class="['fa fa-fw', { 'fa-check': sort == 'status' }]"></i>
              Status
            </a>
          </div>
        </div>
        <div class="dropdown" v-if="environments.length > 1">
          <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown">
            Environments ({{ environmentsFilter.length || "all" }})
            <span class="caret"></span>
          </button>
          <div class="dropdown-menu" role="menu">
            <a
              class="dropdown-item"
              href="#"
              v-for="environment in environments"
              v-on:click="toggleEnvironmentFilter(environment, $event)"
            >
              <i v-bind:class="['fa fa-fw', { 'fa-check': environmentsFilter.indexOf(environment) != -1 }]"></i>
              {{ environment }}
            </a>
          </div>
        </div>
      </div>
      <div class="col text-center" v-if="environments.length === 1">
        <span
          class="lead"
          v-bind:title="'Showing instances of environment ' + environments[0]"
          data-bs-toggle="tooltip"
          >{{ environments[0] }}</span
        >
      </div>
      <div class="col">
        <p class="text-secondary text-end mt-2 mb-0 me-4">
          <i v-if="loading" class="fa fa-spinner fa-spin loader"></i>
          <span :title="refreshDate ? 'last refresh at ' + refreshDate.format('HH:mm:ss') : ''"
            >Refreshed every 1m</span
          >
        </p>
      </div>
    </div>

    <div class="row">
      <div
        v-for="(instance, instanceIndex) in filteredInstances"
        :key="instance.hostname + instance.pg_port"
        ref="cards"
        v-cloak
        class="col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 pb-3"
      >
        <InstanceCard
          v-bind:instance="instance"
          v-bind:status_value="getStatusValue(instance)"
          v-bind:refreshInterval="refreshInterval"
          v-bind:index="instanceIndex"
          v-bind:start="start"
          v-bind:end="end"
          ref="instanceCards"
        ></InstanceCard>
      </div>
    </div>
    <div v-if="!loading && instances.length == 0" class="row justify-content-center" v-cloak>
      <div class="col col-12 col-sm-10 col-md-6 col-lg-4 text-body-secondary text-center">
        <h4 class="m-4">No instance</h4>
        <template v-if="isAdmin">
          <p>No instance is available yet.</p>
          <p>
            Go to
            <strong><a href="/settings/instances">Settings</a></strong> to add or configure instances.
          </p>
        </template>
        <template v-if="!isAdmin">
          <p>You don't have access to any instance.</p>
          <p>Please contact an administrator.</p>
        </template>
      </div>
    </div>
  </div>
</template>
