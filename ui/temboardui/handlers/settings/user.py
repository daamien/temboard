from temboardui.application import (
    add_role,
    add_role_in_group,
    check_role_email,
    check_role_name,
    check_role_password,
    check_role_phone,
    hash_password,
)
from temboardui.errors import TemboardUIError
from temboardui.web.tornado import admin_required, app


@app.route(r"/json/settings/user", methods=["POST"])
@admin_required
def create_user(request):
    data = request.json
    validate_user_data(data)

    h_passwd = handle_password(data)
    role = add_role(
        request.db_session,
        data["new_username"],
        h_passwd,
        data["email"],
        data["phone"],
        data["is_active"],
        data["is_admin"],
    )
    add_user_to_groups(request, data, role)
    return {"message": "OK"}


def validate_user_data(data, role=None):
    # Submited attributes checking.
    if not data.get("new_username"):
        raise TemboardUIError(400, "Username is missing.")
    if data.get("email"):
        check_role_email(data["email"])
    if data.get("phone"):
        check_role_phone(data["phone"])
    if "groups" not in data:
        raise TemboardUIError(400, "Groups field is missing.")
    if "is_active" not in data:
        raise TemboardUIError(400, "Active field is missing.")
    if "is_admin" not in data:
        raise TemboardUIError(400, "Administrator field is missing.")

    if role and role.role_name != data["new_username"]:
        if not data.get("password"):
            raise TemboardUIError(
                400, "Username will be changed, you need to change " "the password too."
            )
    if role is None:
        if not data.get("password"):
            raise TemboardUIError(400, "Password is missing.")
    if data.get("password") and not data.get("password2"):
        raise TemboardUIError(400, "Password confirmation is missing.")
    if "password" in data and "password2" in data:
        if data["password"] != data["password2"]:
            raise TemboardUIError(400, "Password confirmation can not be checked.")
    if data["groups"] is not None and not isinstance(data["groups"], list):
        raise TemboardUIError(400, "Invalid group list.")

    check_role_name(data["new_username"])


def handle_password(data):
    if data["password"]:
        check_role_password(data["password"])
        return hash_password(data["new_username"], data["password"]).decode("utf-8")
    return None


def add_user_to_groups(request, data, role):
    if data["groups"]:
        for group_name in data["groups"]:
            add_role_in_group(request.db_session, role.role_name, group_name)
