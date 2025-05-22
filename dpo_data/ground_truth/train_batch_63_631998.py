import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().segment((-56,-92),(80,-92)).segment((80,41)).arc((70,45),(61,53)).segment((31,53)).arc((-57,81),(-56,-12)).close().assemble().finalize().extrude(-97).union(w0.sketch().push([(12,-20)]).circle(20).push([(6,-23)]).circle(6,mode='s').finalize().extrude(103))