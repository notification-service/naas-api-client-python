# Naas Python API Client

## Usage

The client is broken down into several concerns:

* [Configuration](#configuration): This provides the ability to set some defaults or configure as needed per-request.
* [Routing](#routing): By using the **API Directory**, we can show all available routes.
* [Logging](#logging): Setting up several log specifications for use with the client.
* [Connection](#connection): This is the main HTTP/TCP connection to the underlying service.
* [Requests](#requests): These are the raw _requests_ from the API service.
* [Responses](#responses): These are the raw _responses_ form the API service request.
* [Error Handling](#error-handling): These are all of the errors and exceptions that could be encountered.
* [Modeling](#modeling): These are the domain models wrapped around the _response_ from the API service.

## Configuration
The configuration can happen per instance or at a global level per application. This permits us to use with a single `access_token` in another context, or to use multiple clients.

You can review the configuration code to see what options are available and what _sensible defaults_ are used.

> TODO: Write the configuration object that can be used throughout.

## Routing
Routing is handle by reading the Directory from the API Service. This returns all fully qualified URIs and [URI Templates](https://tools.ietf.org/html/rfc6570). By keeping the routing management in a single place, we eliminate the need to manually construct URIs with string building or string interpolation. Some examples:

```python
# List out the link relationships
>>> directory = naas.models.Directory.retrieve()
>>> for link in directory.links():
>>>   print(link.rel())

# Retrieve a route for a specified link relationship
>>> link = directory.links().route_for('http://naas-api-local.deviceindependent.com/rels/projects')
<naas.models.link.Link object at 0x103b5db00>
>>> link.url_for()
'http://naas-api-local.deviceindependent.com/projects'

# Check if the route is templates
>>> link.templated()
True

# Return a URL with provided params
>>> link.url_for({ 'page': 1, 'per_page': 3 })
'http://naas-api-local.deviceindependent.com/projects?page=1&per_page=3'

```

By using _named routes_ (`rel`) we reduce the risk that URIs change with the API Service. We only ever need to know the `rel` and the underlying API Service will manage what that points to.

## Logging
As the client may be used in different contexts, this permits us to use our customized `Logger` and log to different contexts (`Logger`, `STDOUT`, etc). There are several logs that can be specified:

* `request_logger`: This will log all of the raw HTTP requests. The underlying HTTP dependency uses `requests` and these are the logs that our output from these requests.
* `logger`: This is where all activity is logged within the `package` itself
* `cache_logger`: When enabled and supported, this is where caching would log the _hits_ and _misses_.

You may choose to point them all to the same log or have separate logs. The goal is to keep the separation of logging concerns.

> TODO: Write the logging object

## Connection

> The python `requests` package does not include a separate concern for connection. While this is an important aspect and we would want a re-usable connection object, we have to use the _requests_ themselves.

## Requests
This is where HTTP requests get issued. There are several things to note here:

* Not all requests will be returning `JSON` domain models. This means it may be more important to get the raw _response_ to work with the `body` or `headers.
* Some requests support pagination, and you can use the built-in tools of the client to _follow_ links. For example, you can use the client to **auto paginate** by following the `links` with a `rel` of `next` until none exists.
* You should be aware of the possible HTTP status code responses. 
* There are helper methods directly off of the `Client` itself to perform the basic operations.

Here are some examples:

```python
# Make a request to the projects
>>> naas.Client.get('http://naas-api-local.deviceindependent.com/projects')
<Response [200]>

# Make a head request
>>> naas.Client.head('http://naas-api-local.deviceindependent.com/projects')
<Response [200]>
```

> TODO: Implement the `post`, `put`, `patch`, `options` methods.


There are also specific `Request` objects based on the **domain models**

```python
# Retrieve the directory
>>> naas.requests.Directory.retrieve()
<Response [200]>
```

> TODO: Implement the `Request` objects for all domain models

## Responses

These are the [`Response` objects](http://docs.python-requests.org/en/master/api/#requests.Response) returned from the `Request` itself.

```python
# Retrieve the status code
>>> request = naas.requests.Directory.retrieve()
>>> request.status_code
200

# Content (truncated for brevity)
>>> request.content
>>> b'{"data":{"title":"Notifications as a Service API"}}'

# JSON response
>>> request.json()
{'data': {'title': 'Notifications as a Service API' } }

# Headers
>>> request.headers
{'X-Frame-Options': 'SAMEORIGIN', 'X-XSS-Protection': '1; mode=block', 'X-Content-Type-Options': 'nosniff', 'X-Download-Options': 'noopen', 'X-Permitted-Cross-Domain-Policies': 'none', 'Referrer-Policy': 'strict-origin-when-cross-origin', 'Content-Type': 'application/vnd.naas.json; charset=utf-8', 'ETag': 'W/"ef1bdaf3531d46fb47cbd0ddbca29fd6"', 'Cache-Control': 'max-age=0, private, must-revalidate', 'X-Request-Id': '61aa8def-73f2-4344-93d1-4276756bd32d', 'X-Runtime': '0.010917', 'Vary': 'Accept-Encoding, Origin', 'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked'}

# Status OK?
>>> request.ok
True

# Final URL (after any redirects)
>>> request.url
'http://naas-api-local.deviceindependent.com/'
```

> TODO: Implement handling of all possible responses (2XX success, 3XX redirection, 4XX error, 5XX server error)

## Error Handling
Things can go wrong. We want to ensure a consistent fashion for handling:

* HTTP errors from the API Service
* Exceptions from our library or underlying dependencies

By doing so we can ensure the consumer of this client library will not have to know about underlying dependencies or issues. We can also use this to raise custom exceptions and `Error` objects within the library. An example is:

> TODO: Implement the set of possible exceptions (`RecordNotFoundError`, `RecordInvalidError`, `SystemError`, etc)


## Modeling
These are the domain models that represent the `body` from the [request](#requests). We may support different models depending on the serialization (`JSON`, `CSV`, `PNG`, etc). 

> Currently we only support JSON domain models

Every object that has a response has a corresponding model:

* `Links`: This is a collection of `Link` objects. Wherever there is embedded hypermdia, this will be returned. Links can also be extracted from the `Link` HTTP header.
* `Pagination`: This is the object that corresponds to any pagination information on _lists_ of data. It gives the upper and lower bounds as well as total amount.
* `Data`: This is the main object that will correspond to a _list_ (collection) or _instance_ of an object. These models then support extended modeling.
* `Error`: This is the object that will return `ErrorItems` (collection) and `ErrorItem` (instance) records when an HTTP error occurs. This model is always the same.
* `Query`: This will support the query that gets sent to the server when performing a _search_. This will echo back the Query specified, based on the supported HTTP parameters

> Query is not yet supported

These models return the type-casted values of the attributes (`Boolean`, `DateTime`, `Date`, `Time`, `String`, `Integer`, etc).

Some examples:

```python
# Retrieve the directory
>>> directory = naas.models.Directory.retrieve()
<naas.models.directory.Directory object at 0x10288e908>

# Return the title attribute
>>> directory.title()
'Notifications as a Service API'

# Return the description
>>> directory.description()
'API for notfications as a service'

# Return the links collection
>>> directory.links()
<naas.models.links.Links object at 0x1028d92e8>

# Total number of links
>>> len(list(directory.links()))
32

# List out the link titles
>>> for link in directory.links():
...   print(link.title())
... 
Directory
Link Relationships
Link Relationship
Account
Account Settings
Account Settings Enable SendGrid
Account Settings Disable SendGrid
SMTP Settings
SMTP Setting
Primary SMTP Setting
Projects
Project
Project Campaigns
Project Campaign
Project Campaign Email Templates
Project Campaign Email Template
Subscribers
Subscriber
Subscriber Email Addresses
Subscriber Email Address
Primary Subscriber Email Address
Confirm Subscriber Email Address
Email Addresses
Email Address
Email Notifications
Email Notification
Email Notification Preview
Email Notification Deliver
Email Notification Deliveries
Email Notification Delivery Status
Email Notification Delivery
Email Notification Basic
```

