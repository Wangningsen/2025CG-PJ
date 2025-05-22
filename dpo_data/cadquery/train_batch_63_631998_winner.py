import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().segment((-56,-92),(80,-92)).segment((80,41)).arc((73,43),(67,47)).segment((67,53)).segment((30,53)).arc((-56,82),(-56,-10)).close().assemble().finalize().extrude(-97).union(w0.sketch().push([(12,-20)]).circle(20).push([(9,-23)]).circle(4,mode='s').finalize().extrude(103))