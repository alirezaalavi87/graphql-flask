from api import app, db
# from api import models
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, QueryType, MutationType
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.queries import listPosts_resolver, getPost_resolver
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver

explorer_html = ExplorerGraphiQL().html(None)

query = QueryType()
query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)

mutation = MutationType()
mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # On GET request serve the GraphQL explorer.
    return explorer_html, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    print(result)
    status_code = 200 if success else 400
    return jsonify(result), status_code