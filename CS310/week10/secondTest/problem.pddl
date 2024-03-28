(define (problem strathclyde-taxi-problem) 
  (:domain strathclyde-taxis)
  (:objects
    royal_college graham_hills tic barony_hall livingstone_tower - location
    taxi_1 taxi_2 - taxi
    alice bob charlie dave emma frank - person
  )
  (:init
    (at-taxi taxi_1 tic) 
    (at-taxi taxi_2 royal_college)
    (empty taxi_1)
    (empty taxi_2)

    ; People at their initial locations
    (at-person alice royal_college) 
    (at-person bob livingstone_tower)
    (at-person charlie barony_hall)
    (at-person dave graham_hills)
    (at-person emma tic)
    (at-person frank livingstone_tower)

    ; Define the sequence of locations
    (next royal_college graham_hills)
    (next graham_hills tic)
    (next tic barony_hall)
    (next barony_hall livingstone_tower)
    (next livingstone_tower royal_college)
  )
  (:goal
    (and
      (at-person alice graham_hills)
      (at-person bob barony_hall)
      (at-person charlie tic)
      (at-person dave livingstone_tower)
      (at-person emma royal_college)
      (at-person frank barony_hall)
    )
  )
)