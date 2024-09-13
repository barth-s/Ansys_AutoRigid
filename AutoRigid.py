    tag = "_rig"
    bodies = ExtAPI.DataModel.Tree.GetObjectsByType(DataModelObjectCategory.Body)
    for obj in bodies: 
        if str(obj.Name).endswith(tag) :
            obj.StiffnessBehavior = StiffnessBehavior.Rigid
        else :
            obj.StiffnessBehavior = StiffnessBehavior.Flexible
    ExtAPI.DataModel.Tree.Refresh()