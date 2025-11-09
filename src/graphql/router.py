import strawberry
from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter

from ..core.database import get_db
from .user.schema import UserQuery, UserMutation


async def get_graphql_context(
    db: Session = Depends(get_db)
):
    """
    Context getter for GraphQL.
    Provides database session to GraphQL resolvers.
    """
    return {"db": db}

@strawberry.type
class Query(UserQuery):
    """Root GraphQL Query type."""
    pass

@strawberry.type
class Mutation(UserMutation):
    """Root GraphQL Mutation type."""
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_router = GraphQLRouter(
    schema,
    context_getter=get_graphql_context,
)
