---
title: "Models"
url: "https://platform.minimax.io/docs/guides/models-intro.md"
site: "platform.minimax.io"
type: "doc"
via: "direct"
---
> ## Documentation Index
> Fetch the complete documentation index at: https://platform.minimax.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Models

> Overview of MiniMax AI models and their capabilities

### Language

| **Models**           | **Description**           | **Features**                 |
| :- | :- | :- |
| [MiniMax-M3.1-Flash](https://platform.minimax.io/docs/api-reference/text-anthropic-api.md) | Frontier multimodal coding model with 1M context window and tunable thinking depth | • Multimodal • 1M context window • Frontier coding • Tunable thinking depth |
| [MiniMax-M3](https://platform.minimax.io/docs/api-reference/text-anthropic-api.md) | Frontier multimodal coding model with 1M context window | • Multimodal • 1M context window • Frontier coding |

### Video

| **Models**             | **Description**                   | **Res.& Dur.**         | **FPS**         |
| :- | :- | :- | :- |
| [MiniMax-H3](https://platform.minimax.io/docs/api-reference/video-generation-v2-create.md) | Next-gen open general-purpose multimodal video model • Text-to-Video / Image-to-Video / First–Last Frame / Multimodal reference | • 768P / 2K • 4–15s | 24 fps |

> [accordion] Legacy Models
>
> | **Models**             | **Description**                   | **Res.& Dur.**         | **FPS**         |
> | :- | :- | :- | :- |
> | [MiniMax Hailuo 2.3](https://platform.minimax.io/docs/api-reference/video-generation-t2v.md) | • Text to Video & Image to Video • SOTA instruction following • Extreme physics mastery | • 1080p 6s • 768p 6s, 10s | 24 fps |
> | [MiniMax Hailuo 2.3Fast](https://platform.minimax.io/docs/api-reference/video-generation-i2v.md) | •  Image to Video • Extreme physics mastery • Value and Efficiency | • 1080p 6s • 768p 6s, 10s | 24 fps |
> | [MiniMax Hailuo 02](https://platform.minimax.io/docs/api-reference/video-generation-t2v.md) | • Text to Video & Image to Video • SOTA instruction following • Extreme physics mastery | • 1080p 6s • 768p 6s, 10s • 512p 6s, 10s | 24 fps |

### Image

| **Models**             | **Description**           | **Features**                           |
| :- | :- | :- |
| [MiniMax-H3-Image](https://platform.minimax.io/docs/api-reference/image-generation-h3-generations.md) | • Text-to-Image & Image Edit • 1–16 reference images | • Output size by width and height, or by area tier and aspect ratio • Streaming output |
| [MiniMax-H3-Image-Highspeed](https://platform.minimax.io/docs/api-reference/image-generation-h3-generations.md) | • High-speed version of MiniMax-H3-Image • Text-to-Image & Image Edit | • Same parameters and limits as MiniMax-H3-Image |

> [accordion] Legacy Models
>
> | **Models**             | **Description**           | **Features**                           |
> | :- | :- | :- |
> | [image-01](https://platform.minimax.io/docs/api-reference/image-generation-t2i.md) | • Text-to-Image & Image-to-Image | • Fine-grained image detail |
> | [image-01-live](https://platform.minimax.io/docs/api-reference/image-generation-i2i.md) | • Image-to-Image | • Enhanced styles such as hand-drawn and cartoon |

### Audio

| **Models**             | **Description**           | **Features**                           |
| :- | :- | :- |
| [speech-2.8-hd](https://platform.minimax.io/docs/api-reference/speech-t2a-http.md) | • Ultra-realistic quality featuring sound tags | • 40 languages supported • 7 emotions supported • specified languages and dialects supported |
| [speech-2.8-turbo](https://platform.minimax.io/docs/api-reference/speech-t2a-http.md) | • Seamless speed meets natural flow | • 40 languages supported • 7 emotions supported • specified languages and dialects supported |

> [accordion] Legacy Models
>
> | **Models**             | **Description**           | **Features**                           |
> | :- | :- | :- |
> | [speech-2.6-hd](https://platform.minimax.io/docs/api-reference/speech-t2a-http.md) | • Ultimate Similarity • Ultra-High Quality | • 40 languages supported • 7 emotions supported • specified languages and dialects supported |
> | [speech-2.6-turbo](https://platform.minimax.io/docs/api-reference/speech-t2a-http.md) | • Ultimate Value • Low latency | • 40 languages supported • 7 emotions supported • specified languages and dialects supported |
> | [speech-02-hd](https://platform.minimax.io/docs/api-reference/speech-t2a-http.md) | • Stronger replication similarity • High quality voice generation | • 24 languages supported • 7 emotions supported • specified languages and dialects supported |
> | [speech-02-turbo](https://platform.minimax.io/docs/api-reference/speech-t2a-http.md) | • Superior rhythm and stability • Low latency | • 24 languages supported • 7 emotions supported • specified languages and dialects supported |

### Music

> [!NOTE]
>
> Starting August 20, 2026, the paid APIs (Music Generation and Lyrics Generation) will no longer be available to new users; existing paying users can continue to use the current API services. The free music generation APIs (Music-3.0-free, Music-2.6-free, music-cover-free) will be discontinued.
>
> To experience or use music generation capabilities, please visit [MiniMax Audio](https://www.minimax.io/audio), or use the open-source [MiniMax Music 3 model on Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-Music3).

| **Models**             | **Description**           | **Features**                           |
| :- | :- | :- |
| [music-3.0](https://platform.minimax.io/docs/api-reference/music-generation) | • New Music Generation Capabilities | • Intent Understood • Sound Elevated • Vocals Humanized |
| [music-2.6](https://platform.minimax.io/docs/api-reference/music-generation) | • Cover Reborn. Bass Redefined. | • Cover Reborn. Bass Redefined. |
| [music-cover](https://platform.minimax.io/docs/api-reference/music-generation) | • Generate cover versions from reference audio | • One-step cover generation • Two-step cover with lyrics modification • Style transfer • Auto lyrics extraction |

> [accordion] Legacy Models
>
> | **Models**             | **Description**           | **Features**                           |
> | :- | :- | :- |
> | [music-2.0](https://platform.minimax.io/docs/api-reference/music-generation) | • Text to Music • Enhanced musicality • Natural vocals and smooth melodies | • Human-like performance • Rich emotional expression • Enhanced tone control |

