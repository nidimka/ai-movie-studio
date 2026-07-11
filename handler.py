import runpod

def handler(job):
    print("Received job:", job)

    return {
        "status": "success",
        "message": "AI Movie Studio Serverless is alive!"
    }

runpod.serverless.start({
    "handler": handler
})
