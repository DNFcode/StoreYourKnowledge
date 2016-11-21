let id = 0

export const createGoal = () => {
  type: "CREATE_GOAL",
  id: id++
}

export const editGoal = (id, name) => {
  type: "EDIT_GOAL",
  id,
  name
}

export const removeGoal = (id) => {
  type: "REMOVE_GOAL",
  id
}
