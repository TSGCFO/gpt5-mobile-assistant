---
url: "https://platform.openai.com/docs/guides/image-generation?image-generation-model=dall-e-2"
title: "Image generation - OpenAI API"
---

Log in [Sign up](https://platform.openai.com/signup)

# Image generation

Learn how to generate or edit images.

Copy page

## Overview

The OpenAI API lets you generate and edit images from text prompts, using the GPT Image or DALL·E models. You can access image generation capabilities through two APIs:

### Image API

The [Image API](https://platform.openai.com/docs/api-reference/images) provides three endpoints, each with distinct capabilities:

- **Generations**: [Generate images](https://platform.openai.com/docs/guides/image-generation#generate-images) from scratch based on a text prompt
- **Edits**: [Modify existing images](https://platform.openai.com/docs/guides/image-generation#edit-images) using a new prompt, either partially or entirely
- **Variations**: [Generate variations](https://platform.openai.com/docs/guides/image-generation#image-variations) of an existing image (available with DALL·E 2 only)

This API supports `gpt-image-1` as well as `dall-e-2` and `dall-e-3`.

### Responses API

The [Responses API](https://platform.openai.com/docs/api-reference/responses/create#responses-create-tools) allows you to generate images as part of conversations or multi-step flows. It supports image generation as a [built-in tool](https://platform.openai.com/docs/guides/tools?api-mode=responses), and accepts image inputs and outputs within context.

Compared to the Image API, it adds:

- **Multi-turn editing**: Iteratively make high fidelity edits to images with prompting
- **Flexible inputs**: Accept image [File](https://platform.openai.com/docs/api-reference/files) IDs as input images, not just bytes

The image generation tool in responses only supports `gpt-image-1`. For a list of mainline models that support calling this tool, refer to the [supported models](https://platform.openai.com/docs/guides/image-generation#supported-models) below.

### Choosing the right API

- If you only need to generate or edit a single image from one prompt, the Image API is your best choice.
- If you want to build conversational, editable image experiences with GPT Image, go with the Responses API.

Both APIs let you [customize output](https://platform.openai.com/docs/guides/image-generation#customize-image-output) — adjust quality, size, format, compression, and enable transparent backgrounds.

DALL·E 2 is our oldest image generation model and therefore has significant
limitations. For a better experience, we recommend using [GPT\\
Image](https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1).

### Model comparison

Our latest and most advanced model for image generation is `gpt-image-1`, a natively multimodal language model.

We recommend this model for its high-quality image generation and ability to use world knowledge in image creation. However, you can also use specialized image generation models—DALL·E 2 and DALL·E 3—with the Image API.

| Model | Endpoints | Use case |
| --- | --- | --- |
| DALL·E 2 | Image API: Generations, Edits, Variations | Lower cost, concurrent requests, inpainting (image editing with a mask) |
| DALL·E 3 | Image API: Generations only | Higher image quality than DALL·E 2, support for larger resolutions |
| GPT Image | Image API: Generations, Edits – Responses API support coming soon | Superior instruction following, text rendering, detailed editing, real-world knowledge |

This guide focuses on DALL·E 2, but you can also switch to the docs for [GPT\\
Image](https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1) and [DALL·E\\
3](https://platform.openai.com/docs/guides/image-generation?image-generation-model=dall-e-3).

![a vet with a baby otter](https://cdn.openai.com/API/docs/images/otter.png)

## Generate Images

You can use the [image generation endpoint](https://platform.openai.com/docs/api-reference/images/create) to create images based on text prompts. To learn more about customizing the output (size, quality, format, transparency), refer to the [customize image output](https://platform.openai.com/docs/guides/image-generation#customize-image-output) section below.

You can set the `n` parameter to generate multiple images at once in a single request (by default, the API returns a single image).

Generate an image

python

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
import OpenAI from "openai";
const openai = new OpenAI();

const result = await openai.images.generate({
  model: "dall-e-3",
  prompt: "a white siamese cat",
  size: "1024x1024",
});

console.log(result.data[0].url);
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
11
12
from openai import OpenAI
client = OpenAI()

result = client.images.generate(
    model="dall-e-2",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(result.data[0].url)
```

```bash
1
2
3
4
5
6
7
8
9
curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "dall-e-2",
    "prompt": "a white siamese cat",
    "n": 1,
    "size": "1024x1024"
  }'
```

## Edit Images

The [Image Edits](https://platform.openai.com/docs/api-reference/images/createEdit) endpoint lets you edit parts of an image by uploading an image and mask indicating which areas should be replaced. This process is also known as **inpainting**.

You can provide a mask to indicate where the image should be edited. The transparent areas of the mask will be replaced, while the filled areas will be left unchanged.

You should use the prompt to describe the full new image, **not just the erased area**.

Edit an image

python

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

const result = await openai.images.generate({
  model: "dall-e-2",
  prompt: "a white siamese cat",
  n: 1,
  size: "1024x1024",
});

console.log(result.data[0].url);
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
11
12
13
from openai import OpenAI
client = OpenAI()

result = client.images.edit(
    model="dall-e-2",
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
    n=1,
    size="1024x1024",
)

print(result.data[0].url)
```

```bash
1
2
3
4
5
6
7
8
curl https://api.openai.com/v1/images/edits \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F model="dall-e-2" \
  -F image="@sunlit_lounge.png" \
  -F mask="@mask.png" \
  -F prompt="A sunlit indoor lounge area with a pool containing a flamingo" \
  -F n=1 \
  -F size="1024x1024"
```

| Image | Mask | Output |
| --- | --- | --- |
| ![A pink room with a pool](https://cdn.openai.com/API/images/guides/image_edit_original.webp) | ![A mask in part of the pool](https://cdn.openai.com/API/images/guides/image_edit_mask.webp) | ![The original pool with an inflatable flamigo replacing the mask](https://cdn.openai.com/API/images/guides/image_edit_output.webp) |

Prompt: a sunlit indoor lounge area with a pool containing a flamingo

#### Mask requirements

The mask must be a square PNG image and less than 4MB in size.

The mask image must also contain an alpha channel. If you're using an image editing tool to create the mask, make sure to save the mask with an alpha channel.

Add an alpha channel to a black and white mask

You can modify a black and white image programmatically to add an alpha channel.

Add an alpha channel to a black and white mask

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
from PIL import Image
from io import BytesIO

# 1. Load your black & white mask as a grayscale image
mask = Image.open(img_path_mask).convert("L")

# 2. Convert it to RGBA so it has space for an alpha channel
mask_rgba = mask.convert("RGBA")

# 3. Then use the mask itself to fill that alpha channel
mask_rgba.putalpha(mask)

# 4. Convert the mask into bytes
buf = BytesIO()
mask_rgba.save(buf, format="PNG")
mask_bytes = buf.getvalue()

# 5. Save the resulting file
img_path_mask_alpha = "mask_alpha.png"
with open(img_path_mask_alpha, "wb") as f:
    f.write(mask_bytes)
```

### Image Variations

Available for DALL·E 2 only, the [image variations](https://platform.openai.com/docs/api-reference/images/createVariation) endpoint allows you to generate a variation of a given image.

Generate an image variation

python

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

const result = await openai.images.createVariation({
  model: "dall-e-2",
  image: fs.createReadStream("corgi_and_cat_paw.png"),
  n: 1,
  size: "1024x1024"
});

console.log(result.data[0].url);
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
11
from openai import OpenAI
client = OpenAI()

result = client.images.create_variation(
    model="dall-e-2",
    image=open("corgi_and_cat_paw.png", "rb"),
    n=1,
    size="1024x1024"
)

print(result.data[0].url)
```

```bash
1
2
3
4
5
6
curl https://api.openai.com/v1/images/variations \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F model="dall-e-2" \
  -F image="@corgi_and_cat_paw.png" \
  -F n=1 \
  -F size="1024x1024"
```

| Image | Output |
| --- | --- |
| ![A cat and a dog](https://cdn.openai.com/API/images/guides/image_variation_original.webp) | ![A similar cat and dog](https://cdn.openai.com/API/images/guides/image_variation_output.webp) |

Similar to the edits endpoint, the input image must be a square PNG image less than 4MB in size.

## Customize Image Output

You can configure the following output options:

- **Size**: Image dimensions (e.g., `1024x1024`, `1024x1536`)
- **Quality**: Rendering quality (e.g. `standard`)
- **Format**: `url` (default), `b64_json`

### Size and quality options

Square images with standard quality are the fastest to generate. The default size is 1024x1024 pixels.

|     |     |
| --- | --- |
| Available sizes | \- `256x256` \- `512x512` \- `1024x1024` (default) |
| Quality options | \- `standard` (default) |

### Output format

The default Image API output when using DALL·E 2 is a url pointing to the hosted image.
You can also request the `response_format` as `b64_json` for a base64-encoded image.

## Limitations

DALL·E 2 is our first image generation model and therefore has significant limitations:

- **Text Rendering:** The model struggles with rendering legible text.
- **Instruction Following:** The model has trouble following instructions.
- **Realism:** The model is not able to generate realistic images.

For a better experience, we recommend using [GPT Image](https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1) for image generation.

## Cost and latency

Cost for DALL·E 2 is fixed can be calculated by image generated depending on the size.

You can find the pricing details on the [pricing page](https://platform.openai.com/pricing#image-generation).

DALL-E 2