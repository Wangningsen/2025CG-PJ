import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().push([(-46.5,0)]).rect(95,200).push([(-47,0)]).circle(19,mode='s').finalize().extrude(-76).union(w0.sketch().arc((42,-1),(41,-41),(81,-46)).segment((91,-35)).arc((83,2),(46,3)).arc((47,-2),(42,-1)).assemble().push([(63.5,-21.5)]).rect(17,13,mode='s').finalize().extrude(-6))