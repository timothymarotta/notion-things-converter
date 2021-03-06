import enum
from Helper import Helper

class ThingsActions(enum.Enum):
    note = 1
    header = 2
    item = 3
    children = 4
    none = 5

class ThingsModel():
    # class variable; should not be in __init__ function because it is constant to the class, does not change by object
    model = {
        'paragraph': ThingsActions.note,
        'heading_1': ThingsActions.header,
        'heading_2': ThingsActions.header,
        'heading_3': ThingsActions.header,
        'bulleted_list_item': ThingsActions.item,
        'numbered_list_item': ThingsActions.item,
        'to_do': ThingsActions.item,
        'toggle': ThingsActions.children,
        'child_page': ThingsActions.none,
        'unsupported': ThingsActions.none
    }

    # model keys will not be inserted, updated, or deleted, so only access modifiers are unnecessary
    
    # method to get action enum from model
    # PARAM action_name: string of block name
    # RETURN enum
    @classmethod
    def get_action(self, action_name):
        try:
            return self.model[action_name]
        except KeyError:
            return None
    
    @classmethod 
    def get_model(self):
        return self.model 
            
# the methods of this class are to be used AFTER a block is retrieved from Notion to convert ONLY to Things 3; other destinations will require their own Helpers
# implements Helper abstract class
class ThingsHelper(Helper):
    model = ThingsModel()

    def convert_to_heading(self):
        pass

    def convert_to_notes(self):
        pass

    def convert_to_item(self):
        pass
