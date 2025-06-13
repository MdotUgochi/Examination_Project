from uuid import uuid4
from typing import Dict, List, Any


db:  Dict[str, List[Dict[str, Any]]] = {
    "users": [],
    "events": [],
    "speakers": [{
            "id": str(uuid4()),
            "name": "Prof Helen Owoaje",
            "topic": "The effects of climate change on public health"
              
        },
        {
            "id": str(uuid4()),
            "name": "Aisha Garuwa",
            "topic": "Artificial Intelligence and the future of finance"
        
        }, 
        {
            "id": str(uuid4()),
            "name": "Joshua Kingsley",
            "topic": "Cybersecurity Awareness in the age of Artificial Intelligence"
         
        }],
    "registrations": [],
}