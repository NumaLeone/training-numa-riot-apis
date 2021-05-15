const riotKey = "api_key=api-key";
const sp = "%20";
const fetch = require("node-fetch");

async function fetchBySumName(name, ch) {
  console.log("starting");
  // turns name into link format
  //   while (name.includes("")) {
  //     let spaceSpot = name.indexOf(" ");
  //     name = name.substring(0, spaceSpot) + sp + name.substring(spaceSpot + 1);
  //   }

  //request to riot's api
  console.log("request to riot's api");
  const link =
    "https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +
    name +
    "?" +
    riotKey;
  // no me funciona  "https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/${name}?${riotKey}"
  const response = await fetch(link);

  // turns the return value to json
  console.log("turns the return value to json");
  let data = await response.json();
  console.log(data);

  if (ch == "id") {
    console.log("wrong one reached");
    return data.id;
  } else if (ch == "accountId") {
    return data.accountId;
  } else if (ch == "puuuId") {
    return data.puuuId;
  } else if ((ch = "name")) {
    return data.name;
  } else if (ch == "profileIconId") {
    return data.profileIconId;
  } else if (ch == "revisionDate") {
    return data.revisionDate;
  } else if (ch == "summonerLevel") {
    return data.summonerLevel;
  } else {
    console.log("ch is not valid");
    return null;
  }
}

//fetchBySumName("Rafternot", "accountId");

async function getMatchList(
  accId,
  champId,
  queue,
  endTime,
  beginTime,
  endIndex,
  beginIndex
) {
  //link building
  let link =
    "https://la2.api.riotgames.com/lol/match/v4/matchlists/by-account/" +
    (await accId) +
    "?";

  if (champId != null) link += "champion=" + champId + "&";
  if (queue != null) link += "queue=" + queue + "&";
  if (endTime != null) link += "endtime=" + endTime + "&";
  if (beginTime != null) link += "beginTime=" + beginTime + "&";
  if (endIndex != null) link += "endIndex=" + endIndex + "&";
  if (beginIndex != null) link += "beginIndex=" + beginIndex + "&";

  link += riotKey;

  //use link to grab info

  let response = await fetch(link);
  response = await response.json();
  //get the champion from the last match you played
  //console.log(response.matches[0].champion);
  //get list of all the matches
  //console.log(response);
  //get the last match you played
  console.log(response.matches[0]);
}

// async function sth() {
//   let link = "https://127.0.0.1:2999/replay/game";
//   let response = await fetch(link);
//   response = await response.json();
//   console.log(response);
// }
// sth();
getMatchList(fetchBySumName("Rafternot", "accountId"));
