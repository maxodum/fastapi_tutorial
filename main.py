from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/',
         summary='Root',
         operation_id='root__get')
def root():
    return ""

@app.post('/post',
        summary='Get Post',
        operation_id='get_post_post_post',
        response_model=Timestamp)
def post() -> Timestamp:
    time = post_db[-1]
    time = Timestamp(id = time.id + 1, timestamp = time.timestamp + 1)
    post_db.append(time)
    return time


@app.get('/dog',
         summary='Get Dogs',
         operation_id='get_dogs_dog_get',
         response_model=list[Dog])
def get_dogs(kind:DogType = None) -> list[Dog]:
    selected = []
    if kind is not None:
        for i in range(len(dogs_db)):
            if dogs_db[i].kind == kind:
                selected.append(dogs_db[i])
    else:
        for i in range(len(dogs_db)):
            selected.append(dogs_db[i])
    return selected


@app.post('/dog',
          summary='Create Dog',
          operation_id='create_dog_dog_post',
          response_model=Dog)
def create_dog(dog: Dog):
    dogs_db[len(dogs_db)] = dog
    return dog


@app.get('/dog/{pk}', 
        summary='Get Dog By Pk',
        operation_id='get_dog_by_pk_dog__pk__get',
        response_model=Dog)
def get_dog_by_pk(pk:int) -> Dog:
    for i in range(len(dogs_db)):
        if dogs_db[i].pk == pk:
            return dogs_db[i]


@app.patch('/dog/{pk}',
          summary='Update Dog',
          operation_id='update_dog_dog__pk__patch',
          response_model=Dog)
def update_dog(pk:int, dog: Dog):
    for i in range(len(dogs_db)):
        if dogs_db[i].pk == pk:
            dogs_db[i] = dog
            return dog
