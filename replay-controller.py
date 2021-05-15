# riotKey = "api_key-RGAPI-6b697fac-77d3-49e7-bc35-00d76113a965"

import requests
import json

url = "https://127.0.0.1:2999/replay/render"

payload = json.dumps({
    "cameraMode": "fps",
    "cameraPosition": {
        "x": 1000,
        "y": 21000,
        "z": 6000
    },
    "cameraRotation": {
        "x": 0,
        "y": 90,
        "z": 0
    }
})
headers = {
    'api_key': 'api-key',
    'Content-Type': 'application/json'
}

response = requests.request(
    "POST", url, headers=headers, data=payload, verify=False)

print(response.text)

# {
#         "cameraAttached": false,
#         "cameraLookSpeed": 1.0,
#         "cameraMode": "fps",
#         "cameraMoveSpeed": 500.0,
#         "cameraPosition": {
#                 "x": 1000.0,
#                 "y": 21000.0,
#                 "z": 7000.0
#         },
#         "cameraRotation": {
#                 "x": 0.0,
#                 "y": 90.0,
#                 "z": 0.0
#         },
#         "characters": true,
#         "depthFogColor": {
#                 "a": 1.0,
#                 "b": 0.0,
#                 "g": 0.0,
#                 "r": 0.0
#         },
#         "depthFogEnabled": false,
#         "depthFogEnd": 8000.0,
#         "depthFogIntensity": 1.0,
#         "depthFogStart": 5000.0,
#         "depthOfFieldCircle": 10.0,
#         "depthOfFieldDebug": false,
#         "depthOfFieldEnabled": false,
#         "depthOfFieldFar": 5000.0,
#         "depthOfFieldMid": 2000.0,
#         "depthOfFieldNear": 0.0,
#         "depthOfFieldWidth": 800.0,
#         "environment": true,
#         "farClip": 24250.0,
#         "fieldOfView": 40.0,
#         "floatingText": true,
#         "fogOfWar": true,
#         "healthBarChampions": true,
#         "healthBarMinions": true,
#         "healthBarPets": true,
#         "healthBarStructures": true,
#         "healthBarWards": true,
#         "heightFogColor": {
#                 "a": 1.0,
#                 "b": 0.0,
#                 "g": 0.0,
#                 "r": 0.0
#         },
#         "heightFogEnabled": false,
#         "heightFogEnd": -100.0,
#         "heightFogIntensity": 1.0,
#         "heightFogStart": 300.0,
#         "interfaceAll": true,
#         "interfaceAnnounce": true,
#         "interfaceChat": false,
#         "interfaceFrames": true,
#         "interfaceMinimap": true,
#         "interfaceQuests": false,
#         "interfaceReplay": true,
#         "interfaceScore": true,
#         "interfaceScoreboard": false,
#         "interfaceTarget": true,
#         "interfaceTimeline": true,
#         "navGridOffset": 0.0,
#         "nearClip": 50.0,
#         "outlineHover": true,
#         "outlineSelect": true,
#         "particles": true,
#         "skyboxOffset": 0.0,
#         "skyboxPath": "ASSETS/Maps/Skyboxes/Riots_SRU_Skybox_CubeMap.dds",
#         "skyboxRadius": 2500.0,
#         "skyboxRotation": 0.0,
#         "sunDirection": {
#                 "x": 0.25,
#                 "y": -0.75,
#                 "z": 0.05000000074505806
#         }
# }

# sth
