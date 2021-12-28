from django.shortcuts import render
from django.views import View
import os
from instagramy import InstagramUser
from instagramy import InstagramHashTag
from instagramy import InstagramLocation
from instagramy import InstagramPost
from .forms import Form
from instagramy.core.requests import get


def get_mainpage(request):
	return render(request, "insta/MainPage.html")


class Analyze(View):
	def get(self, request, Choose):
		form = Form()
		return render(request, "insta/MainPage.html", {"form": form, "choose": Choose})
	
	
	def post(self, request, Choose):
		form = Form(request.POST)
		if form.is_valid():
			text = form.cleaned_data["text"]
			session_id = form.cleaned_data["sessionid"]
			if Choose == "UserInfo":
				user = InstagramUser(text, sessionid=session_id)
				context = {
					"Username": user.username,
					"Fullname": user.fullname,
					"Biography": user.biography,
					"Website": user.website,
					"Number of Mutual Follower": user.no_of_mutual_follower,
					"Number of Followers": user.number_of_followers,
					"Number of Followings": user.number_of_followings,
					"Number of Posts": user.number_of_posts,
					"Is Privated": user.is_private,
					"Connected Facebook Page": user.connected_fb_page,
					"Followed By Viewer": user.followed_by_viewer,
					"Follows Viewer": user.follows_viewer,
					"Has Blocked Viewer": user.has_blocked_viewer,
					"Has Country Block": user.has_country_block,
					"Has Requested Viewer": user.has_requested_viewer,
					"Has Blocked By Viewer": user.is_blocked_by_viewer,
					"Is Joined Recently": user.is_joined_recently,
					"Is Verified": user.is_verified,
					"Other Info": user.other_info,
					"Posts": user.posts,
					"Posts Display URLs": user.posts_display_urls,
					"Profile Picture URL": user.profile_picture_url,
					"Requested By Viewer": user.requested_by_viewer,
					"Restricted By Viewer": user.restricted_by_viewer,
					"Viewer": user.viewer,
				}
			elif Choose == "Post":
				post = InstagramPost(text, sessionid=session_id)
				context = {
					"Author": post.author,
				}
				try:
					context.update({
						"Caption": post.caption,
					})
				except:
					pass
				context.update({
					"Type of Post": post.type_of_post,
					"Upload Time": post.upload_time,
					"Number of Comments": post.number_of_comments,
					"Number of Likes": post.number_of_likes,
					"Display Url": post.display_url,
					"Post Source": post.post_source,
					"Text": post.text,
					"Viewer": post.viewer,
				})
				try:
					location_id, slug = post.location.id, post.location.slug
					location = InstagramLocation(location_id, slug)
					context.update({
						"Address": location.address,
						"LocationID": location.id,
						"Latitude": location.latitude,
						"Longitude": location.longitude,
						"URL": location.url,
						"Viewer": location.viewer,
						"Website": location.website,
						"Name": location.name,
						"Number of Posts": location.number_of_posts,
						"Phone": location.phone,
						"Slug": location.slug,
						"Top Posts": location.top_posts,
						"Profile Picture URL": location.profile_pic_url
					})
				except:
					pass
			else:
				tag = InstagramHashTag(text)
				context = {
					"Number of Posts": tag.number_of_posts,
					"Posts Display URLs": tag.posts_display_urls,
					"Profile Picture URL": tag.profile_pic_url,
					"Tag Name": tag.tagname,
					"Top Posts": tag.top_posts,
					"Viewer": tag.viewer,
				}
			return render(request, "insta/MainPage.html", {"form": form, "context": context, "choose": Choose})
		return render(request,"insta/MainPage.html", {"form": form})

