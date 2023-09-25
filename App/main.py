from fastapi import FastAPI
from App.Config.Database import db
from App.Config.Cors import init_cors
from App.Graphql import Mutation, Query
import strawberry
from strawberry.fastapi import GraphQLRouter


def init_app() -> FastAPI:

    app = FastAPI(
        title="FastAPI Template",
        description="Template for FastAPI projects",
         version="0.1.0",
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    init_cors(app)

    @app.get("/")
    def home():
        return {"message": "Hello World"}

    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema=schema)
    app.include_router(graphql_app, prefix="/graphql")
    return app

app = init_app()
