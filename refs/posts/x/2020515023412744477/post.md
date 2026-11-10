---
title: "Thank me later:"
author: "Delba (@delba_oliveira)"
date: "2026-02-08"
url: "https://x.com/delba_oliveira/status/2020515023412744477"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Thank me later:
- Warcraft Peon: https://www.wowhead.com/sounds/name:peasant
- Warcraft Peasant: https://www.wowhead.com/sounds/name:peon
- Mario: https://www.myinstants.com/en/search/?name=mario
- Spongebob: https://www.myinstants.com/en/search/?name=spongebob

- -
E.g:

//.claude/settings.json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /Users/d/.claude/hooks/PeonReady1.wav"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /Users/d/.claude/hooks/PeonYes3.wav"
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /Users/d/.claude/hooks/PeonWhat3.wav"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /Users/d/.claude/hooks/PeonBuildingComplete1.wav"
          }
        ]
      }
    ]
  }
}
