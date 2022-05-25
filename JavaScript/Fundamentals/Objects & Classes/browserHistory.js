//@ts-check

/**
 * @param {object} browser
 * @param {array} operations
 */
function browserHistory(browser, operations) {
    operations.forEach((operation) => {
        if (operation === "Clear History and Cache") {
            browser["Open Tabs"] = [];
            browser["Recently Closed"] = [];
            browser["Browser Logs"] = [];
        } else {
            let action = operation.split(" ")[0];
            let target = operation.split(" ")[1];
            switch (action) {
                case "Open":
                    browser["Open Tabs"].push(target);
                    browser["Browser Logs"].push(operation);
                    break;
                case "Close":
                    let openTabs = Object.values(browser)[1];
                    if (openTabs.includes(target)) {
                        openTabs.splice(openTabs.indexOf(target), 1);
                        browser["Recently Closed"].push(target);
                        browser["Browser Logs"].push(operation);
                    }
                    break;
            }
        }
    });
    console.log(Object.values(browser)[0]);
    console.log(`Open Tabs: ${Object.values(browser)[1].join(", ")}`);
    console.log(`Recently Closed: ${Object.values(browser)[2].join(", ")}`);
    console.log(`Browser Logs: ${Object.values(browser)[3].join(", ")}`);
}

// browserHistory(
//     {
//         "Browser Name": "Google Chrome",
//         "Open Tabs": ["Facebook", "YouTube", "Google Translate"],
//         "Recently Closed": ["Yahoo", "Gmail"],
//         "Browser Logs": [
//             "Open YouTube",
//             "Open Yahoo",
//             "Open Google Translate",
//             "Close Yahoo",
//             "Open Gmail",
//             "Close Gmail",
//             "Open Facebook",
//         ],
//     },
//     ["Close Facebook", "Open StackOverFlow", "Open Google"]
// );

browserHistory(
    {
        "Browser Name": "Mozilla Firefox",
        "Open Tabs": ["YouTube"],
        "Recently Closed": ["Gmail", "Dropbox"],
        "Browser Logs": [
            "Open Gmail",
            "Close Gmail",
            "Open Dropbox",
            "Open YouTube",
            "Close Dropbox",
        ],
    },
    ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]
);
