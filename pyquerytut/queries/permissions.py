from bridgekeeper import perms
from bridgekeeper.rules import is_authenticated, Attribute, Relation, ManyRelation, Is
from .models import Organization

is_public_course = ManyRelation(
    "organizations", "organizations", Organization, Attribute("name", matches="MITx")
)

perms["queries.view_course"] = is_authenticated | is_public_course
