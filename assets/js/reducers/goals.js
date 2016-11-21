import OrderedMap from 'immutable'

const goals = (state = new OrderedMap(), action) => {
  switch (action.type) {
    case "CREATE_GOAL":
      return state.set(action.id, "new goal")
    case "EDIT_GOAL":
      return state.set(action.id, action.name)
    case "REMOVE_GOAL":
      return state.delete(action.id)
    default:
      return state
  }
}
