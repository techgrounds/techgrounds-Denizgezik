# SNS, SQS, EventBridge

Welk probleem lost X op? <br>
Welke key termen horen bij X? <br>
Hoe past X / vervangt X in een on-premises setting? <br>
Hoe kan ik X combineren met andere diensten? <br>
Wat is het verschil tussen X en andere gelijksoortige diensten? <br>

Een handige lijst van taken die je praktisch moet kunnen: <br>
Waar kan ik deze dienst vinden in de console? <br>
Hoe zet ik deze dienst aan? <br>
Hoe kan ik deze dienst koppelen aan andere resources? <br>

## Key-terms

QUEUE:

Een <b>QUEUE</b> (Engels voor wachtrij) is in de informatica een datastructuur voor de opslag van een wisselend aantal elementen waarbij geldt dat het element dat het eerst werd toegevoegd het eerst wordt verwijderd (FIFO).

API:

Een <b>API</b>, of een Application Programming Interface, wordt gebruikt om op een geformaliseerde manier gegevens uit te wisselen tussen apps. Veel voorzieningen bieden openbare API's waarmee iedereen inhoud naar de voorziening kan sturen en van de voorziening kan ontvangen.


<b>SQS = Simple Queue Service.</b>

This service works one to one. 

It is used for <b>One to One</b> reliable asynchronous service and basically allow search to DECOUPLE our business application stuff. 

Has 3 parameters:

- Message <br>
- Queue <br>
- Polling <br>

<b>SNS = Simple Notification Service </b>

It allows one to many (this is the major difference with SQS).<br>
Provides us an High Throughput & allows to have Many Subscribers.

Ideal for building scalable enterprise applications.

Has 4 parameters:
- Publish <br>
- Message <br>
- Topics <br>
- Subscribe <br>
<br>

<b>EVENTBRIDGE</b>

It allows to have <b>One to Many</b> kind of communication. 
But the Many here is restricted to 5! <br>
So for a specific rule you have a maximun of 5 targets.

It also allows to filter messages, defined rules so that we can based on the parameters or the conditions, within the incoming message, we can decide what should be the destination target for that message
(makes it very suitable for SaaS, Application Integrations e.g. MongoDB Atlas).

It has 4 parameters:
- Message Bus <br>
- Events <br>
- Rules <br>
- Targets <br>

Message Bus = basically a container for your events. <br>

Events = an event is a record of an action that has happened in the past: in this context it is represented as a Json object that contains data from the event and metadata about the event.
Events can be constructed either by an application such as order service can also be emmitted by a aws service itsel like ec2 for example.<br>
Event is like a pending or shipped or delivery event. <br>

Rules = basically just match incoming events and sends them to their corresponding targets for processing.<br>

Targets = are your destination endpoints. Subscribers 


Free integration with third-party services like Shopify, PagerDuty, Datadog. 

IN GENERAL:

Why does it have to Decouple applications?

- Loose Coupling:

Decoupling through SQS promotes loose coupling between components. Each component only needs to understand the message format and the queue structure, not the internal implementation details of other components. This makes it easier to evolve and update components without affecting the entire system.

- Decoupled Release Cycles: <br>

When components are decoupled, they can have independent release cycles. Teams can update or release new versions of components without affecting the entire system, provided they maintain compatibility with the messages exchanged via SQS.

- Interoperability: <br>

Decoupling allows for better interoperability between different services or systems. As long as components adhere to the agreed-upon message format, they can be implemented in different languages or technologies.

<br>

SNS, SQS, EventBridge: 

BASICALLY THESE ARE THE THREE SERVICES THAT ARE AVAILABLE AWS WHICH ONE WOULD USE FOR <b> DECOUPLING OF APPLICATIONS </b> AND <b>TO BUILT AN ENTERPRISE READY SCALABLE ECOSYSTEM</b>. 


## Opdracht
### Gebruikte bronnen

- https://www.youtube.com/watch?v=4Nr29Kz8N6c

- https://www.youtube.com/watch?v=RoKAEzdcr7k


### Ervaren problemen


### Resultaat


- Chatgpt:

<b>"Fan-out"</b> is a term commonly used in distributed systems and messaging architectures to describe the process of broadcasting a message to multiple consumers or downstream components. It's the opposite of "fan-in," where multiple sources send messages to a single destination.

In the context of messaging systems like Amazon Simple Queue Service (SQS) or publish-subscribe patterns, fan-out typically refers to the ability to send a message from one producer to multiple consumers or subscribers.


- SNS :

![Alt text](06_includes/SNS.png)


- When to use what?

![Alt text](<06_includes/When to use what.png>)

Event Bus:

![Alt text](<06_includes/Event Bus.png>)

