use std::process::Command;


#[allow(unused)]
fn commend()
{
Command::new("cmd")                         // programe name.
        .args(&["/C", "cls"])                   // Arguments as string iterable refrence.
        .status();                                          // Execute the commend and get the status as Result enum.
}
