import cadquery as cq
w0=cq.Workplane('YZ',origin=(51,0,0))
r=w0.sketch().arc((14,-15),(35,-17),(50,-2)).segment((60,-2)).segment((60,10)).segment((50,10)).segment((49,12)).segment((47,11)).arc((40,22),(29,27)).arc((-44,32),(14,-15)).assemble().finalize().extrude(-102).union(w0.sketch().push([(-50,-41.5)]).rect(100,31).push([(83,-17)]).circle(17).finalize().extrude(-60))