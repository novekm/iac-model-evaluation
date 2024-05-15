import aws_cdk as core
import aws_cdk.assertions as assertions

from dynamodb_global_index.dynamodb_global_index_stack import DynamodbGlobalIndexStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dynamodb_global_index/dynamodb_global_index_stack.py
def test_dynamodb_global_index_created():
    app = core.App()
    stack = DynamodbGlobalIndexStack(app, "dynamodb-global-index")
    template = assertions.Template.from_stack(stack)