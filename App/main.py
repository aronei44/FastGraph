from fastapi import FastAPI
from App.Config.Database import db
from App.Config.Cors import init_cors
from App.Graphql import Mutation, Query, Subscription
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL


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

    schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
    graphql_app = GraphQLRouter(
        schema,
        subscription_protocols=[
            GRAPHQL_TRANSPORT_WS_PROTOCOL,
            GRAPHQL_WS_PROTOCOL,
        ],
    )
    app.include_router(graphql_app, prefix="/graphql")
    return app

app = init_app()
