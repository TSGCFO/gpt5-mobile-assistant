---
url: "https://platform.openai.com/docs/guides/priority-processing"
title: "Priority processing - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Priority processing

Get faster processing in the API with flexible pricing.

Copy page

Priority processing gives significantly lower, more consistent latency compared to Standard processing while keeping pay-as-you-go flexibility.

Priority processing is ideal for high-value, user-facing applications with regular traffic where latency is paramount. Priority processing should not be used for data processing, evaluations, or other highly erratic traffic.

Create a response with priority processing

python

```bash
1
2
3
4
5
curl https://api.openai.com/v1/responses   -H "Authorization: Bearer $OPENAI_API_KEY"   -H "Content-Type: application/json"   -d '{
    "model": "gpt-5",
    "input": "What does 'fit check for my napalm era' mean?",
    "service_tier": "priority"
  }'
```

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
import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
  model: "gpt-5",
  input: "What does 'fit check for my napalm era' mean?",
  service_tier: "priority"
});

console.log(response);
```

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
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="What does 'fit check for my napalm era' mean?",
    service_tier="priority"
)
print(response)
```

Responses contain the assigned tier for the request. Requests that cannot be handled by priority processing will be assigned `default`, or `priority` if they were assigned for priority processing.

## Rate limits and ramp rate

**Baseline limits**

Priority consumption is treated like Standard for rate‑limit accounting. Use your usual retry and backoff logic. For a given model, the rate limit is shared between Standard and Priority processing.

**Ramp rate limit**

If your traffic ramps too quickly, some Priority requests may be downgraded to Standard and billed at Standard rates. The response will show service\_tier="default". Currently, the ramp rate limit may apply if you’re sending at least 1 million TPM and >50% TPM increase within 15 minutes. To avoid triggering the ramp rate limit, we recommend:

- Ramp gradually when changing models or snapshots
- Use feature flags to shift traffic over hours, not instantly.
- Avoid large ETL or batch jobs on Priority

## Usage considerations

- Per token costs are billed at a premium to standard - see [pricing](https://platform.openai.com/docs/pricing) for more information.
- Cache discounts are still applied for priority processing requests.
- Priority processing applies for multimodal / image input requests as well.
- Requests handled with priority processing can be viewed in the dashboard using the "group by service tier" option.
- See the [pricing page](https://platform.openai.com/docs/pricing) for which models currently support Priority processing.
- Long context, fine-tuned models and embeddings are not yet supported.

We use cookies and similar technologies to deliver, maintain, improve our services and for security purposes. Check our [Cookie Policy](https://openai.com/policies/cookie-policy) for details. Click 'Accept all' to let OpenAI and partners use cookies for these purposes. Click 'Reject all' to say no to cookies, except those that are strictly necessary. Choose 'Manage Cookies' to pick specific cookies you're okay with or to change your preferences.

Reject allAccept all