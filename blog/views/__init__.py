from .blog_views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView, garbage
from .blogger_views import BloggerListView, BloggerDetailView, BloggerUpdateView, BloggerDeleteView
from .index import index
from .user_views import UserDetailView, UserUpdateView, UserDeleteView
from .application_views import ApplicationCreateView, ApplicationAllListView, \
    ApplicationPendingListView, ApplicationUserListView, \
        ApplicationDetailView, ApplicationDeleteView, ApplicationUpdateView, ApplicationRejectView, application_accept
from .comment_views import CommentCreateView, CommentDeleteView
