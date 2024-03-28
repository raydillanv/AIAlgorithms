(define (domain strathclyde-taxis)
  (:requirements :strips)
  (:predicates
    (at-taxi ?taxi ?loc) ; Taxi location
    (at-person ?person ?loc) ; Person location
    (inside ?person ?taxi) ; Person is inside a specific taxi
    (empty ?taxi) ; Taxi is empty, still used for managing get-in and get-out actions
    (next ?from ?to) ; Directly adjacent locations for sequential movement
  )

  ; Move taxi from one location to the next in sequence
  (:action move
    :parameters (?taxi ?from ?to)
    :precondition (and
      (at-taxi ?taxi ?from)
      (next ?from ?to)) ;
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
      (empty ?taxi) ; Ensuring taxi is marked as empty after someone gets out
      (at-person ?person ?loc))
  )
)