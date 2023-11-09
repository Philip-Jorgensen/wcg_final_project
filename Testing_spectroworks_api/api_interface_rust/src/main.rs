#[allow(unused_imports)]

use serde_json::{Result, Value};

// Global variables
const API_KEY: &str = "ZWZhMWQ1MTQtOGM4MS00YzI1LWJiY2UtNTg3YWY1MGI5ZmQ0";

struct Connection<'a> {
    api_key: &'a str,
    url: &'a str,
    client: reqwest::blocking::Client,
}

#[derive(serde::Deserialize)]
struct Ip {
    text: String,
}

impl Connection<'_> {
    fn get_projects(&self) -> Result<()> {
        let raw_url = format!("{}list_projects?api_key={}",self.url, self.api_key);
        let res = self.client.get(&raw_url[..])
            .send();
        let res = match res {
            Ok(a) => a.json::<Ip>(),
            Err(error) => panic!("{}", error),
        };

        // let res_body = res.json::<Ip>().text;

        println!("{:#?}", res);

        // let v: Value = serde_json::from_str(res)?;
       
        // println!("{:#?}", v);

        Ok(())
    }
}

fn main() {
    let connection = Connection{
        api_key: API_KEY,
        url: "https://api.spectroworks.com/prod/api/",
        client: reqwest::blocking::Client::new(),
    };

    let _ = connection.get_projects();
}
