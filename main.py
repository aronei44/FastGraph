import uvicorn
from fastapi import FastAPI
from Config.Database import db
from Graphql.Mutation import Mutation
from Graphql.query import Query
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

    @app.get("/")
    def home():
        return {"message": "Hello World"}
    
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema=schema)

    app.include_router(graphql_app, prefix="/graphql")


    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000, reload=True)