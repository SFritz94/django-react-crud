import { useEffect, useState } from "react"
import { getAllTasks } from '../api/tasks.api'
import TaskCard from '../components/TaskCard'

function TasksList() {
    const [tasks, setTasks] = useState([])

    useEffect(()=>{
        async function loadTasks() {
            const resp = await getAllTasks()
            setTasks(resp.data)
        }
        loadTasks()
    }, [])

  return (
    <div className="grid grid-cols-3 gap-3">
        {tasks.map(task => (
            <TaskCard key={task.id} task={task}/>
        ))}
    </div>
  )
}

export default TasksList