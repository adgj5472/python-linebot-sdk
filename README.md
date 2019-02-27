# python-linebot-sdk

## *更新
2019-2-26 更新 
- MemberJoinEvent
- MemberLeaveEvent

## Webhook event object

https://developers.line.me/en/docs/messaging-api/reference/#webhook-event-objects

### Event

- MessageEvent
    - type
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - message: `Message <#message>`__
- FollowEvent
    - type
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
- UnfollowEvent
    - type
    - timestamp
    - source: `Source <#source>`__
- JoinEvent
    - type
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
- LeaveEvent
    - type
    - timestamp
    - source: `Source <#source>`__
- PostbackEvent
    - type
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - postback: Postback
        - data
        - params: dict
- BeaconEvent
    - type
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - beacon: Beacon
        - type
        - hwid
        - device_message  
        
***New**        
 - MemberJoinEvent
 
 - MemberLeaveEvent

### Source

- SourceUser
    - type
    - user\_id
- SourceGroup
    - type
    - group\_id
    - user\_id
- SourceRoom
    - type
    - room\_id
    - user\_id

### Message

- TextMessage
    - type
    - id
    - text
- ImageMessage
    - type
    - id
- VideoMessage
    - type
    - id
- AudioMessage
    - type
    - id
- LocationMessage
    - type
    - id
    - title
    - address
    - latitude
    - longitude
- StickerMessage
    - type
    - id
    - package\_id
    - sticker\_id
- FileMessage
    - type
    - id
    - file\_size
    - file\_name
```
