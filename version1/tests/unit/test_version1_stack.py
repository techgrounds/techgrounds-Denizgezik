import aws_cdk as core
import aws_cdk.assertions as assertions

from version1.version1_stack import Version1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in version1/version1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Version1Stack(app, "version1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
