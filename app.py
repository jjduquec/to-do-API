from fastapi import FastAPI,HTTPException   
from typing import Optional,List,Union
from pydantic import BaseModel,Field



app=FastAPI() 

task_list=[{"id":1,
            "title":"mi primera tarea",
            "description":"mi primer tarea en la app"}
            ]

class Task(BaseModel): 
    title:str 
    description:str  


class TaskCreate(Task): 
    title:str=Field(
        ...,
        min_length=4,  
        max_length=100,
        examples=["Esto es una tarea de ejemplo"]
    )

    description:Optional[str]=Field(
        min_length=4,
        max_length=500

    )  

class TaskPublic(Task): 
    id:int  

class TaskSummary(BaseModel): 
    id:int  
    title:str  

@app.get("/tasks",response_model=List[Task])
def get_tasks(): 
    if len(task_list)>0:  
        return task_list  
    raise HTTPException(status_code="204",description="No hay tareas registradas")
    

@app.get("/task/{id}",response_model=Union[TaskPublic,TaskSummary]) 
def get_task(id:int,description:bool=False):
    for task in task_list: 
        if task["id"]==id:  
          
            if description:  
                
                return {"id":task["id"],
                        "title":task["title"],
                        "description":task["description"]}
            else:  
                return {"id":task["id"],
                        "title":task["title"]
                        }

    return HTTPException(status_code="404",description="Tarea no encontrada")    
     

      

