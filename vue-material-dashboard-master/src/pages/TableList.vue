<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100">
        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Subscription Table</h4>
            <p class="category">Manage your subscriptions</p>
          </md-card-header>
          <md-card-content>
            <table>
              <thead>
                <tr>
                  <th>User ID</th>
                  <th>Topic</th>
                  <th>Email</th>
                  <th>Phone</th>
                  <th>Subscription Date</th>
                  <th>Active</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="subscription in subscriptions" :key="subscription.id">
                  <td>{{ subscription.user_id }}</td>
                  <td>{{ subscription.topic }}</td>
                  <td>{{ subscription.email }}</td>
                  <td>{{ subscription.phone }}</td>
                  <td>{{ subscription.subscription_date }}</td>
                  <td>{{ subscription.active }}</td>
                  <td>
                    <button @click="openModal(subscription)">Edit</button>
                    <button @click="deleteSubscription(subscription.id)">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
            <button @click="openModal()">Add Subscription</button>
          </md-card-content>
        </md-card>
      </div>
    </div>

    <!-- Modal for adding/editing subscriptions -->
    <div v-if="isModalOpen" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>{{ currentSubscription.id ? 'Edit' : 'Add' }} Subscription</h2>
        <form @submit.prevent="saveSubscription">
          <label for="user_id">User ID:</label>
          <input v-model="currentSubscription.user_id" type="number" required />

          <label for="topic">Topic:</label>
          <input v-model="currentSubscription.topic" type="text" required />

          <label for="email">Email:</label>
          <input v-model="currentSubscription.email" type="email" required />

          <label for="phone">Phone:</label>
          <input v-model="currentSubscription.phone" type="text" required />

          <label for="subscription_date">Subscription Date:</label>
          <input v-model="currentSubscription.subscription_date" type="date" required />

          <label for="active">Active:</label>
          <select v-model="currentSubscription.active">
            <option value="active">Active</option>
            <option value="inactive">Inactive</option>
          </select>

          <button type="submit">{{ currentSubscription.id ? 'Update' : 'Create' }}</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      subscriptions: [],
      currentSubscription: {},
      isModalOpen: false,
    };
  },
  created() {
    this.fetchSubscriptions();
  },
  methods: {
    async fetchSubscriptions() {
      try {
        const response = await axios.get('http://localhost:8000/subscriptions/');
        this.subscriptions = response.data;
      } catch (error) {
        console.error('Error fetching subscriptions:', error);
      }
    },
    openModal(subscription = {}) {
      this.currentSubscription = { ...subscription };
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
      this.currentSubscription = {};
    },
    async saveSubscription() {
      try {
        if (this.currentSubscription.id) {
          await axios.put(`http://localhost:8000/subscriptions/${this.currentSubscription.id}`, this.currentSubscription);
        } else {
          await axios.post('http://localhost:8000/subscriptions/', this.currentSubscription);
        }
        this.fetchSubscriptions();
        this.closeModal();
      } catch (error) {
        console.error('Error saving subscription:', error);
      }
    },
    async deleteSubscription(id) {
      try {
        await axios.delete(`http://localhost:8000/subscriptions/${id}`);
        this.fetchSubscriptions();
      } catch (error) {
        console.error('Error deleting subscription:', error);
      }
    },
  },
};
</script>

<style>
.modal {
  display: block; /* Show the modal */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto; /* 15% from the top and centered */
  padding: 20px;
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
</style>
