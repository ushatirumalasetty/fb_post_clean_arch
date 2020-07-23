from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.dtos.dtos import *
class GetUserPostInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    def get_user_post(self, user_id: int):
        user_post_complete_details_dto = self.storage.get_user_post(user_id=user_id)
        get_user_post_reactions_metrics = self.get_user_post_reactions(
            user_post_complete_details_dto)
        get_user_comment_reaction_metrics = self.get_user_comment_reactions(
            user_post_complete_details_dto)
        get_user_comment_replies_metrics = self.get_user_comment_replies(
            user_post_complete_details_dto)
        user_post_details_dict = self.presenter.\
            get_response_for_get_user_post_details(
            user_post_complete_details_dto=user_post_complete_details_dto,
            get_user_comment_reaction_metrics=get_user_comment_reaction_metrics,
            get_user_post_reactions_metrics=get_user_post_reactions_metrics,
            get_user_comment_replies_metrics=get_user_comment_replies_metrics
            )
        return user_post_details_dict

    def get_user_post_reactions(self, user_post_complete_details_dto):
        posts_list = []
        posts = user_post_complete_details_dto.post_dtos
        reactions = user_post_complete_details_dto.reactions_dtos
        for post in posts:
            reaction_list = [reaction.reaction_type for reaction in reactions \
                if reaction.post_id==post.post_id]
            reactions_count = len(reaction_list)
            reaction_list = set(reaction_list)
            reaction_list = list(reaction_list)
            post_reaction_details = PostReactionDto(
                post_id=post.post_id,
                reaction_count=reactions_count,
                reaction_type=reaction_list)
            posts_list.append(post_reaction_details)
        return posts_list

    def get_user_comment_reactions(self,user_post_complete_details_dto):
        comments_list = []
        comments = user_post_complete_details_dto.comment_dtos
        reactions = user_post_complete_details_dto.reactions_dtos
        for comment in comments:
            reaction_list = [reaction.reaction_type for reaction in reactions \
                if reaction.comment_id==comment.comment_id]
            reactions_count = len(reaction_list)
            reaction_list = set(reaction_list)
            reaction_list = list(reaction_list)
            comment_reaction_details = CommentReactionDto(
                comment_id=comment.comment_id,
                reaction_count=reactions_count,
                reaction_type=reaction_list)
            comments_list.append(comment_reaction_details)
        return comments_list

    def get_user_comment_replies(self,user_post_complete_details_dto):
        comments = user_post_complete_details_dto.comment_dtos
        comment_list = []
        replies_list = []
        replies_details_list = []
        for comment in comments:
            if comment.parent_comment == None:
                comment_list.append(comment)
            else:
                replies_list.append(comment)
            replies_count = len(replies_list)
            replies_details = CommentRepliesDto(comment_id=comment.comment_id,
                                                replies_count=replies_count)
            replies_details_list.append(replies_details)
        return replies_details_list