from typing import Any, Text, Dict, List

import pymorphy2
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

morph = pymorphy2.MorphAnalyzer()

TERA_LIST = ['Козлов', 'Лебедев', 'Голубев']
OKY_LIST = ['Окулистов', 'Глазной доктор', 'Лапочкин']
PSY_LIST = ['Психаторов', 'Психологов']


class ActionDoctor(Action):
    def name(self) -> Text:
        return "action_doctor"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any], *args, **kwargs) -> List[Dict[Text, Any]]:
        message = 'Принимают следующие врачи: '
        tag = tracker.slots
        doctor = tag.get('doctor_tag')
        if doctor is not None:
            if morph.parse(doctor)[0].normal_form == 'терапевт':
                message += ','.join(TERA_LIST)
            elif morph.parse(doctor)[0].normal_form == 'окулист':
                message += ','.join(OKY_LIST)
            elif morph.parse(doctor)[0].normal_form == 'психиатр':
                message += ','.join(PSY_LIST)

        dispatcher.utter_message(message)
        return []
