from marshmallow import Schema, fields, validate


class EmployeeSchema(Schema):

    id = fields.Int(dump_only=True)

    user_id = fields.Int(required=True)

    full_name = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=100
        )
    )

    phone = fields.Str(
        required=True,
        validate=validate.Length(
            min=7,
            max=15
        )
    )

    address = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=250
        )
    )

    joining_date = fields.Date(
        load_default=None
    )

    department_id = fields.Int(
        required=True
    )

    designation_id = fields.Int(
        required=True
    )

    status = fields.Str(
        load_default="ACTIVE"
    )

    profile_photo = fields.Str(
        load_default=None,
        allow_none=True
    )


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)