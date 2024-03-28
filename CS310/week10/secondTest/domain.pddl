(define (domain strathclyde-taxis)
  (:requirements :strips)
  (:predicates
    (at-taxi ?taxi ?loc) ; Taxi is at a location
    (at-person ?person ?loc) ; Person is at a location
    (inside ?person ?taxi) ; Person is inside a specific taxi
    (empty ?taxi) ; Taxi is empty
    ; Directly adjacent locations to enforce sequential movement
    (next ?from ?to) ; Indicates ?from is directly before ?to in the sequence
  )

  ; Move taxi from one location to the next in sequence
  (:action move
    :parameters (?taxi ?from ?to)
    :precondition (and 
                    (at-taxi ?taxi ?from) 
                    (next ?from ?to)
    :effect (and 
              (not (at-taxi ?taxi ?from)) 
              (at-taxi ?taxi ?to))
  )

  ; Person gets into the taxi
  (:action get-in
    :parameters (?person ?taxi ?loc)
    :precondition (and 
                    (at-taxi ?taxi ?loc) 
                    (at-person ?person ?loc)
                    (empty ?taxi))
    :effect (and 
              (not (at-person ?person ?loc)) 
              (not (empty ?taxi))
              (inside ?person ?taxi))
  )

  ; Person gets out of the taxi
  (:action get-out
    :parameters (?person ?taxi ?loc)
    :precondition (and 
                    (at-taxi ?taxi ?loc) 
                    (inside ?person ?taxi))
    :effect (and 
              (not (inside ?person ?taxi)) 
              (empty ?taxi)
              (at-person ?person ?loc))
  )
)