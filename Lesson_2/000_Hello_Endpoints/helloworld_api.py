"""Hello World API implemented using Google Cloud Endpoints.

Contains declarations of endpoint, endpoint methods,
as well as the ProtoRPC message class and container required
for endpoint method definition.
"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote


# If the request contains path or querystring arguments,
# you cannot use a simple Message class.
# Instead, you must use a ResourceContainer class
REQUEST_CONTAINER = endpoints.ResourceContainer(
    message_types.VoidMessage,
    name=messages.StringField(1),
)
REQUEST_GREET_CONTAINER = endpoints.ResourceContainer(
    name=messages.StringField(1),
    period=messages.StringField(2),
)

package = 'Hello'


class HelloResponse(messages.Message):
    """String that stores a message."""
    greeting = messages.StringField(1,required=True)

# Define a subclass of remote.Service and decorate it with @endpoints.api
@endpoints.api(name='helloworldendpoints', version='v1',description='tf api')
class HelloWorldApi(remote.Service):
    """Helloworld API v1."""

    @endpoints.method(message_types.VoidMessage, HelloResponse,
        path = "sayHello", http_method='GET', name = "sayHello")
    def say_hello(self, request):
        return HelloResponse(greeting="Hello World this is 9pm")

    @endpoints.method(REQUEST_CONTAINER, HelloResponse,
        path = "sayHelloByName", http_method='GET', name = "sayHelloByName")
    def say_hello_by_name(self, request):
        greet = "Hello {}".format(request.name)
        return HelloResponse(greeting=greet)

    @endpoints.method(REQUEST_GREET_CONTAINER, HelloResponse,
      path = "sayHelloByPeriod", http_method='GET', name = "sayHelloByPeriod")
    def say_hello_by_period(self, request):
        greet = "Guten {} {}!".format(request.period,request.name)
        return HelloResponse(greeting=greet)


APPLICATION = endpoints.api_server([HelloWorldApi])
