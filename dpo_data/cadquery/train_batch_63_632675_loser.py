import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-5,0))
w1=cq.Workplane('XY',origin=(0,0,11))
r=w0.sketch().arc((26,65),(0,-1),(72,14)).arc((74,29),(80,42)).arc((79,52),(75,60)).segment((75,59)).segment((74,59)).segment((74,61)).arc((69,64),(63,68)).arc((61,68),(58,67)).segment((58,8)).segment((26,8)).close().assemble().push([(32,-48)]).circle(20).finalize().extrude(-95).union(w1.sketch().push([(-27.5,65)]).rect(51,70).push([(-27.5,64.5)]).rect(49,69,mode='s').finalize().extrude(-91))