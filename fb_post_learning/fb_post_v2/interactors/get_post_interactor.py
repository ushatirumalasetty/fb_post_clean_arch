from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.dtos.dtos import *    
class GetPostInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    def get_post(self, post_id: int):
        is_post_id_valid = self.storage.validate_post_id(post_id=post_id)
        is_invalid_post_id = not is_post_id_valid
        if is_invalid_post_id:
            self.presenter.raise_invalid_post_id_exception()
            return
        post_complete_details_dto = self.storage.get_post(post_id=post_id)
        get_post_reactions_metrics = self.get_post_reactions(
            post_complete_details_dto)
        get_comment_reaction_metrics = self.get_comment_reactions(
            post_complete_details_dto)
        get_comment_replies_metrics = self.get_comment_replies(
            post_complete_details_dto)
        post_details_dict = self.presenter.get_response_for_get_post_details(
            post_complete_details_dto=post_complete_details_dto,
            get_comment_reaction_metrics=get_comment_reaction_metrics,
            get_post_reactions_metrics=get_post_reactions_metrics,
            get_comment_replies_metrics=get_comment_replies_metrics
            )
        return post_details_dict
            
    def get_post_reactions(self, post_complete_details_dto):
        posts = post_complete_details_dto.post_dtos
        reactions = post_complete_details_dto.reactions_dtos
        reaction_list = [reaction.reaction_type for reaction in reactions \
            if reaction.post_id==posts.post_id]
        reactions_count = len(reaction_list)
        reaction_list = set(reaction_list)
        reaction_list = list(reaction_list)
        post_reaction_details = PostReactionDto(
            post_id=posts.post_id,
            reaction_count=reactions_count,
            reaction_type=reaction_list)
        return post_reaction_details
        
        
    def get_comment_reactions(self,post_complete_details_dto):
        comments_list = []
        comments = post_complete_details_dto.comment_dtos
        reactions = post_complete_details_dto.reactions_dtos
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
        
    def get_comment_replies(self,post_complete_details_dto):
        comments = post_complete_details_dto.comment_dtos
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
