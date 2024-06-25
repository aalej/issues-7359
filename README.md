# Repro for issue 7352

## Versions

platform: macOS Sonoma 14.5<br>
firebase-tools: v13.11.4<br>
gcloud: v476.0.0<br>
cloud-datastore-emulator: v2.3.1

## Steps to reproduce

1. Run `python3.11 -m venv venv`
   - Note: You might have a different version of python installed, try replacing `python3.11` with `python3.12`, or `python<VERSION>`
1. Run `. ./venv/bin/activate`
1. Run `pip install -r requirements.txt`
   - Installs the `requests` library
1. Open a separate terminal and run `gcloud emulators firestore start --host-port=127.0.0.1:54510 --database-mode=datastore-mode`
1. Run `python3 main.py`
   - Prints

```json
{
  "missing": [
    {
      "entity": {
        "key": {
          "partitionId": { "projectId": "testbed-test" },
          "path": [{ "kind": "TestEntity", "id": "5348024557502464" }]
        }
      }
    }
  ],
  "readTime": "2024-06-25T12:39:00.592976Z"
}
```

## Notes

Documentation [reference](https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/lookup#response-body)

1. When using `gcloud --project=testbed-test beta emulators datastore start --use-firestore-in-datastore-mode --host-port=127.0.0.1:54510`
1. Run `. ./venv/bin/activate`
   - You don't have to do this if you're already ran `. ./venv/bin/activate`
1. Running `python3 main.py`
   - Prints

```json
{
  "missing": [
    {
      "entity": {
        "key": {
          "partitionId": { "projectId": "testbed-test" },
          "path": [{ "kind": "TestEntity", "id": "5348024557502464" }]
        }
      },
      "version": "1"
    }
  ],
  "transaction": "EQEAAAAAAAAA"
}
```
