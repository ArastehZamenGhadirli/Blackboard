from django.shortcuts import render
from django.http import JsonResponse
from action.models import User, Blackboard, Image, Text
import json

# Create your views here.


def get_blackboard(request, username):

    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    user = User.objects.get(user_name=username)
    blackboard = Blackboard.objects.get(user=user)

    images = list(Image.objects.filter(black_board=blackboard).values())
    texts = list(Text.objects.filter(black_board=blackboard).values())

    response_data = {
        "blackboard_code": blackboard.code,
        "user": user.user_name,
        "images": images,
        "texts": texts,
    }

    return JsonResponse(response_data)


def add_content(request, username):

    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    data = json.loads(request.body)
    user = User.objects.get(user_name=username)
    blackboard = Blackboard.objects.get(user=user)

    if "iamge_name" in data:
        image = Image.objects.create(
            image_name=data["iamge_name"],
            image_height=data.get("image_height", 100),
            image_width=data.get("image_height", 100),
            black_board=blackboard,
        )
        return JsonResponse({"id": image.id, "message": "Image added successfully"})

    elif "content" in data:
        text = Text.objects.create(
            content=data["content"],
            font_size=data.get("font_size", 12),
            font_color=data.get("font_color", "black"),
            black_board=blackboard,
        )

    def delete_content(request, content_type, content_id):
        if content_type == "image":
            Image.objects.get(id=content_id).delete()
        elif content_type == "text":
            Text.objects.get(id=content_id).delete()
        else:
            return JsonResponse({"error": "Invalid content type"}, status=400)

        return JsonResponse({"message": "Blackboard cleared"})
