<script setup>
// A resource deletion dialog
//
// Fetch resource, present a confirmation dialog and delete the resource if the user confirms.
// Use GET or DELETE verb on same resource URL.
// Reload the page after successful deletion.
import $ from "jquery";
import { computed, ref } from "vue";

import Error from "./Error.vue";
import ModalDialog from "./ModalDialog.vue";

const props = defineProps(["id", "title", "noreload"]);
const emit = defineEmits(["done"]);

function open(url) {
  deleteUrl = url;
  root.value.show();
}
defineExpose({ open });

const root = ref(null);
const error = ref(null);
const failed = ref(false);
const waiting = ref(true);
const disabled = computed(() => waiting.value || failed.value);
const resource = ref(null);
let deleteUrl = null;

function fetch() {
  waiting.value = true;
  $.ajax({
    url: deleteUrl,
    success: (data) => {
      resource.value = data;
    },
    error: (xhr) => {
      error.value.fromXHR(xhr);
      failed.value = true;
    },
  }).always(() => {
    waiting.value = false;
  });
}

function submit() {
  waiting.value = true;
  $.ajax({
    url: deleteUrl,
    type: "DELETE",
    error: (xhr) => {
      error.value.fromXHR(xhr);
    },
    success: () => {
      if (!props.noreload) {
        window.location.reload();
      }
      emit("done");
      root.value.hide();
    },
  });
}

function reset() {
  error.value.clear();
  waiting.value = true;
  failed.value = false;
  deleteUrl = null;
}
</script>

<template>
  <ModalDialog :id="id" :title="title" ref="root" @opening="fetch" @closed="reset">
    <div class="modal-body">
      <Error ref="error" :showTitle="false"></Error>
      <slot v-if="resource" :resource="resource"
        ><p class="fs-5 text-center">Please confirm the deletion of the selected resource.</p></slot
      >
    </div>

    <div class="modal-footer">
      <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancel</button>
      <button id="buttonDelete" class="btn btn-danger ms-auto" type="button" @click="submit" :disabled="disabled">
        Yes, delete
        <i v-if="waiting" class="fa fa-spinner fa-spin loader"></i>
      </button>
    </div>
  </ModalDialog>
</template>
