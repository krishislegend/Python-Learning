(***************************************************)
(*               Associated library                *)
(***************************************************)

import BoolUtils

library Ballot

let one_msg = 
  fun (msg : Message) => 
    let nil_msg = Nil {Message} in
    Cons {Message} msg nil_msg
    
let already_Voted = Int32 1
let not_owner = Int32 2
let one = Uint128 1
    
(***************************************************)
(*             The contract definition             *)
(***************************************************)
contract Ballot
(*  Parameters *)
(owner : ByStr20,
 numberofProp  : Uint128
)

(* Mutable fields *)

field voterWeight : Map ByStr20 Uint256 = Emp ByStr20 Uint256
field voted : Map ByStr20 Bool = Emp ByStr20 Bool 
field votes : Map ByStr20 Uint32 = Emp ByStr20 Uint32
field delegations : Map ByStr20 ByStr20 = Emp ByStr20 ByStr20
field voteCounts : Map Uint32 Uint256 = Emp ByStr20 Uint256

(* Transition 1: Give Right to Vote *)
transition giveRightToVote (voter: ByStr20)
    isAuthorized = builtin eq owner _sender;
    match isAuthorized with
    | True =>
        prs1 = builtin put voterWeight voter one;
    | False => 
        msg  = {_tag : "Not Owner"; _recipient : _sender; _amount : Uint128 0;
              code : not_owner};
        msgs = one_msg msg;
        send msgs
    end 
end

(* Transition 1: Give Right to Vote *)
transition vote (Proposal: Uint256)
    isVoted = builtin get voted _sender;
    match isVoted with
    | True =>
        msg  = {_tag : "Already Voted"; _recipient : _sender; _amount : Uint128 0;
              code : already_Voted};
        msgs = one_msg msg;
        send msgs
    end 
    tmp1 = builtin lt Proposal numberofProp;
    match tmp1 with
    | False =>
        builtin put Voted _sender True;
        builtin put Votes _sender Proposal;
        numofprop = builtin get voteCounts Proposal;
        voteweight = builtin get voterWeight _sender;
        Totalprop = builtin add numbofprop voteweight;
        builtin put voteCounts Proposal TotalProp;
    end     
end

