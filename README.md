# AutoRigid script for Ansys

## Purpose

Workaround for the missing parameter option for the stiffness behaviour of solids in Ansys Mechanical.

## How it works:

**The script below declares all geometries as rigid if their names end with "_rig".**

**It gets triggered after the geometry is updated.** 

This allows parameter studies with rigid bodies. 

## How to use:
0. Temporarily tick the option "Connect/Run Python Code Objects when Mechanical is Launched" under Options -> Mechanical (Revert this after the parameter study)

1. Insert a new Python code script into Ansys mechanical by right clicking on the model tree.

2. Set the "Target Callback" to "After Geometry Changed".

3. Copy the whole content of AutoRigid.py into the body of the "after_geometry_changed(...)" function.

4. Right click on the script in the tree and press 'Connect'.

## License

Published under **MIT License**
