---
url: "https://platform.openai.com/docs/guides/realtime-sip"
title: "Realtime API with SIP - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Realtime API with SIP

Connect to the Realtime API using SIP.

Copy page

[SIP](https://en.wikipedia.org/wiki/Session_Initiation_Protocol) is a
protocol used to make phone calls over the internet. With SIP and the
Realtime API you can direct incoming phone calls to the API.

## Overview

If you want to connect a phone number to the Realtime API,
use a SIP trunking provider (e.g., Twilio). This is a service that converts your phone call
to IP traffic. After you purchase a phone number from your SIP trunking
provider, follow the instructions below.

Start by creating a [webhook](https://platform.openai.com/docs/guides/webhooks) for incoming calls, through your **platform.openai.com** [settings](https://platform.openai.com/settings) \> Project > **Webhooks**.
Then, point your SIP trunk at the OpenAI SIP endpoint, using the project ID
for which you configured the webhook, e.g., `sip:$PROJECT_ID@sip.api.openai.com;transport=tls`.
To find your `$PROJECT_ID`, visit [settings](https://platform.openai.com/settings) \> Project > **General**. That page will display the project ID, which
will have a `proj_` prefix.

When OpenAI receives SIP traffic associated with your project,
your webhook will be fired. The event fired will be a
[`realtime.call.incoming`](https://platform.openai.com/docs/api-reference/webhook-events/realtime/call/incoming) event,
like the example below:

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
POST https://my_website.com/webhook_endpoint
user-agent: OpenAI/1.0 (+https://platform.openai.com/docs/webhooks)
content-type: application/json
webhook-id: wh_685342e6c53c8190a1be43f081506c52 # unique id for idempotency
webhook-timestamp: 1750287078 # timestamp of delivery attempt
webhook-signature: v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4= # signature to verify authenticity from OpenAI

{
  "object": "event",
  "id": "evt_685343a1381c819085d44c354e1b330e",
  "type": "realtime.call.incoming",
  "created_at": 1750287018, // Unix timestamp
  "data": {
    "call_id": "some_unique_id",
    "sip_headers": [\
      { "name": "From", "value": "sip:+142555512112@sip.example.com" },\
      { "name": "To", "value": "sip:+18005551212@sip.example.com" },\
      { "name": "Call-ID", "value": "03782086-4ce9-44bf-8b0d-4e303d2cc590"}\
    ]
  }
}
```

From this webhook, you can accept or reject the call, using the `call_id` value from the webhook.
When accepting the call, you'll provide the needed configuration
(instructions, voice, etc) for the Realtime API session.
Once established, you can set up a WebSocket and monitor the session as usual. The APIs to
accept, reject, monitor, refer, and hangup the call are documented below.

## Accept the call

Use the [Accept call endpoint](https://platform.openai.com/docs/api-reference/realtime-calls/accept-call) to
approve the inbound call and configure the realtime session that will answer it.
Send the same parameters you would send in a
[`create client secret`](https://platform.openai.com/docs/api-reference/realtime-sessions/create-realtime-client-secret)
request, i.e., ensure the realtime model, voice, tools, or instructions are set before bridging the
call to the model.

```bash
1
2
3
4
5
6
7
8
curl -X POST "https://api.openai.com/v1/realtime/calls/$CALL_ID/accept" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "type": "realtime",
        "model": "gpt-realtime",
        "instructions": "You are Alex, a friendly concierge for Example Corp."
      }'
```

The request path must include the `call_id` from the
[`realtime.call.incoming`](https://platform.openai.com/docs/api-reference/webhook_events/realtime/call/incoming)
webhook, and every request requires the `Authorization` header shown above. The
endpoint returns `200 OK` once the SIP leg is ringing and the realtime session
is being established.

## Reject the call

Use the [Reject call endpoint](https://platform.openai.com/docs/api-reference/realtime-calls/reject-call) to
decline an invite when you do not want to handle the incoming call, (e.g., from
an unsupported country code.) Supply the `call_id` path parameter
and an optional SIP `status_code` (e.g., `486` to indicate "busy") in the JSON
body to control the response sent back to the carrier.

```bash
1
2
3
4
curl -X POST "https://api.openai.com/v1/realtime/calls/$CALL_ID/reject" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_code": 486}'
```

If no status code is supplied the API uses `603 Decline` by default. A
successful request responds with `200 OK` after OpenAI delivers the SIP
response.

## Monitor call events

After you accept a call, open a WebSocket connection to the same session to
stream events and issue realtime commands. Note that when connecting to an existing
call using the `call_id` parameter, the `model` argument is not used (as it has already been configured
via the `accept` endpoint).

### WebSocket request

`GET wss://api.openai.com/v1/realtime?call_id={call_id}`

### Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `call_id` | string | Identifier from the `realtime.call.incoming` webhook. |

### Headers

- `Authorization: Bearer YOUR_API_KEY`

The WebSocket behaves exactly like any other Realtime API connection. Send
[`response.create`](https://platform.openai.com/docs/api-reference/realtime_client_events/response/create),
and other client events to control the call, and listen for server events to
track progress. See [Webhooks and server-side controls](https://platform.openai.com/docs/guides/realtime-server-controls)
for more information.

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
import WebSocket from "ws";

const callId = "rtc_u1_9c6574da8b8a41a18da9308f4ad974ce";
const ws = new WebSocket(`wss://api.openai.com/v1/realtime?call_id=${callId}`, {
    headers: {
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
    },
});

ws.on("open", () => {
    ws.send(
        JSON.stringify({
            type: "response.create",
        })
    );
});
```

## Redirect the call

Transfer an active call using the
[Refer call endpoint](https://platform.openai.com/docs/api-reference/realtime-calls/refer-call). Provide the
`call_id` as well as the `target_uri` that should be placed in the SIP `Refer-To`
header (for example `tel:+14155550123` or `sip:agent@example.com`).

```bash
1
2
3
4
curl -X POST "https://api.openai.com/v1/realtime/calls/$CALL_ID/refer" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_uri": "tel:+14155550123"}'
```

OpenAI returns `200 OK` once the REFER is relayed to your SIP provider. The
downstream system handles the rest of the call flow for the caller.

## Hang up the call

End the session with the [Hang up endpoint](https://platform.openai.com/docs/api-reference/realtime-calls/hangup-call)
when your application should disconnect the caller. This endpoint can be used to
terminate both SIP and WebRTC realtime sessions.

```bash
curl -X POST "https://api.openai.com/v1/realtime/calls/$CALL_ID/hangup" \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

The API responds with `200 OK` when it starts tearing down the call.

## Python example

The following is an example of a `realtime.call.incoming` handler. It accepts the call and then logs all the events from
the Realtime API.

Python

Python

Python

python

```python
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
from flask import Flask, request, Response, jsonify, make_response
from openai import OpenAI, InvalidWebhookSignatureError
import asyncio
import json
import os
import requests
import time
import threading
import websockets

app = Flask(__name__)
client = OpenAI(
    webhook_secret=os.environ["OPENAI_WEBHOOK_SECRET"]
)

AUTH_HEADER = {
    "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")
}

call_accept = {
    "type": "realtime",
    "instructions": "You are a support agent.",
    "model": "gpt-realtime",
}

response_create = {
    "type": "response.create",
    "response": {
        "instructions": (
            "Say to the user 'Thank you for calling, how can I help you'"
        )
    },
}

async def websocket_task(call_id):
    try:
        async with websockets.connect(
            "wss://api.openai.com/v1/realtime?call_id=" + call_id,
            additional_headers=AUTH_HEADER,
        ) as websocket:
            await websocket.send(json.dumps(response_create))

            while True:
                response = await websocket.recv()
                print(f"Received from WebSocket: {response}")
    except Exception as e:
        print(f"WebSocket error: {e}")

@app.route("/", methods=["POST"])
def webhook():
    try:
        event = client.webhooks.unwrap(request.data, request.headers)

        if event.type == "realtime.call.incoming":
            requests.post(
                "https://api.openai.com/v1/realtime/calls/"
                + event.data.call_id
                + "/accept",
                headers={**AUTH_HEADER, "Content-Type": "application/json"},
                json=call_accept,
            )
            threading.Thread(
                target=lambda: asyncio.run(
                    websocket_task(event.data.call_id)
                ),
                daemon=True,
            ).start()
            return Response(status=200)
    except InvalidWebhookSignatureError as e:
        print("Invalid signature", e)
        return Response("Invalid signature", status=400)

if __name__ == "__main__":
    app.run(port=8000)
```

## Next steps

Now that you've connected over SIP, use the left navigation or click into these pages to start building your realtime application.

- [Using realtime models](https://platform.openai.com/docs/guides/realtime-models-prompting)
- [Managing conversations](https://platform.openai.com/docs/guides/realtime-conversations)
- [Webhooks and server-side controls](https://platform.openai.com/docs/guides/realtime-server-controls)
- [Realtime transcription](https://platform.openai.com/docs/guides/realtime-transcription)

### Additional Resources

- [JavaScript demo](https://hello-realtime.val.run/)
- [Connect the Realtime SIP Connector to Twilio Elastic SIP Trunking](https://www.twilio.com/en-us/blog/developers/tutorials/product/openai-realtime-api-elastic-sip-trunking)