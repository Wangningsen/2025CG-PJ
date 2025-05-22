import cadquery as cq
w0=cq.Workplane('YZ',origin=(51,0,0))
r=w0.sketch().arc((15,-14),(36,-17),(50,-2)).segment((60,-2)).segment((60,10)).segment((50,10)).arc((43,20),(31,25)).arc((-44,32),(15,-14)).assemble().push([(27.5,-17.5)]).rect(1,1,mode='s').finalize().extrude(-102).union(w0.sketch().push([(-50,-41.5)]).rect(100,31).push([(83,-17)]).circle(17).finalize().extrude(-60))