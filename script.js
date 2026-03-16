async function submitProfileForm(event) {
  event.preventDefault();
  const form = document.getElementById("profile-form");
  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());

  const errorsBox = document.getElementById("form-errors");
  errorsBox.hidden = true;
  errorsBox.innerHTML = "";

  try {
    const res = await fetch("/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (!res.ok || !data.success) {
      const errors = data.errors || [data.error || "Failed to get recommendations."];
      const list = document.createElement("ul");
      errors.forEach((e) => {
        const li = document.createElement("li");
        li.textContent = e;
        list.appendChild(li);
      });
      errorsBox.appendChild(list);
      errorsBox.hidden = false;
      return;
    }

    renderPolicies(data.policies || []);
    renderComparisonTable(data.policies || []);
    document.getElementById("results-section").hidden = false;
    document.getElementById("results-section").scrollIntoView({ behavior: "smooth" });
  } catch (err) {
    errorsBox.textContent = "Unexpected error while contacting the server.";
    errorsBox.hidden = false;
  }
}

function renderPolicies(policies) {
  const container = document.getElementById("policy-ccards") || document.getElementById("policy-cards");
  // Backward-safe: support early typo if element id changes
  container.id = "policy-cards";
  container.innerHTML = "";

  if (!policies.length) {
    container.textContent = "No policies matched your profile.";
    return;
  }

  policies.forEach((p) => {
    const card = document.createElement("article");
    card.className = "policy-card";

    const header = document.createElement("div");
    header.className = "policy-card-header";

    const title = document.createElement("h3");
    title.textContent = p.name;

    const badgeWrap = document.createElement("div");
    const typeBadge = document.createElement("span");
    typeBadge.className = "badge type";
    typeBadge.textContent = p.type;
    const scoreBadge = document.createElement("span");
    scoreBadge.className = "badge score";
    if (typeof p.score === "number") {
      scoreBadge.textContent = `Score ${p.score}`;
    } else {
      scoreBadge.textContent = "Recommended";
    }
    badgeWrap.appendChild(typeBadge);
    badgeWrap.appendChild(scoreBadge);

    header.appendChild(title);
    header.appendChild(badgeWrap);

    const meta = document.createElement("div");
    meta.className = "policy-meta";
    const premiumSpan = document.createElement("span");
    premiumSpan.innerHTML = `<span class="policy-meta-label">Premium:</span> ₹${Number(p.premium).toLocaleString()}`;
    const coverageSpan = document.createElement("span");
    coverageSpan.innerHTML = `<span class="policy-meta-label">Coverage:</span> ₹${Number(p.coverage).toLocaleString()}`;
    meta.appendChild(premiumSpan);
    meta.appendChild(coverageSpan);

    const benefitsTitle = document.createElement("div");
    benefitsTitle.className = "policy-meta-label";
    benefitsTitle.textContent = "Benefits";

    const benefitsList = document.createElement("ul");
    benefitsList.className = "benefits-list";
    (p.benefits || []).forEach((b) => {
      const li = document.createElement("li");
      li.textContent = b;
      benefitsList.appendChild(li);
    });

    card.appendChild(header);
    card.appendChild(meta);
    card.appendChild(benefitsTitle);
    card.appendChild(benefitsList);

    container.appendChild(card);
  });
}

function renderComparisonTable(policies) {
  const tbody = document.querySelector("#comparison-table tbody");
  tbody.innerHTML = "";

  policies.forEach((p) => {
    const row = document.createElement("tr");
    const benefitsText = (p.benefits || []).slice(0, 3).join(", ");

    row.innerHTML = `
      <td>${p.name}</td>
      <td>${p.type}</td>
      <td>₹${Number(p.premium).toLocaleString()}</td>
      <td>₹${Number(p.coverage).toLocaleString()}</td>
      <td>${benefitsText}</td>
    `;
    tbody.appendChild(row);
  });
}

async function submitChat(event) {
  event.preventDefault();
  const input = document.getElementById("chat-question");
  const text = input.value.trim();
  if (!text) return;

  appendChatMessage("user", text);
  input.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question: text })
    });
    const data = await res.json();
    const answer = data.answer || "I could not process that question.";
    appendChatMessage("bot", answer);
  } catch (err) {
    appendChatMessage("bot", "There was a problem contacting the server. Please try again.");
  }
}

function appendChatMessage(role, text) {
  const log = document.getElementById("chat-log");
  const div = document.createElement("div");
  div.className = `chat-message ${role}`;
  const p = document.createElement("p");
  p.textContent = text;
  div.appendChild(p);
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
}

document.addEventListener("DOMContentLoaded", () => {
  const profileForm = document.getElementById("profile-form");
  if (profileForm) {
    profileForm.addEventListener("submit", submitProfileForm);
  }

  const chatForm = document.getElementById("chat-form");
  if (chatForm) {
    chatForm.addEventListener("submit", submitChat);
  }
});

